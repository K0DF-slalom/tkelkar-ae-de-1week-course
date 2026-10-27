"""
Spark Structured Streaming Processor

This is the main application that demonstrates key concepts of Spark Structured Streaming:
1. Reading from multiple source types (socket, file, rate)
2. Applying transformations (parsing, enrichment, aggregation)
3. Writing to PostgreSQL using foreachBatch pattern

Usage:
    spark-submit --packages org.postgresql:postgresql:42.7.1 stream_processor.py [source_type]
    
    source_type: socket | file | rate (default: socket)
"""

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, from_json, to_timestamp, window, avg, sum, count, min, max,
    when, lit, current_timestamp, expr
)
from pyspark.sql.types import (
    StructType, StructField, StringType, DoubleType, IntegerType, TimestampType
)

#CONSTANTS
from config import (
    AGGREGATES_TRIGGER_INTERVAL,
    AGG_CHECKPOINT_DIR,
    CHECKPOINT_BASE_DIR,
    CONSOLE_TRIGGER_INTERVAL,
    FILE_INPUT_DIR,
    FILE_MAX_FILES_PER_TRIGGER,
    POSTGRES_CONFIG,
    RATE_NUM_PARTITIONS,
    RATE_ROWS_PER_SECOND,
    RATE_SYMBOL_MOD,
    RATE_SYMBOLS,
    SOCKET_HOST,
    SOCKET_PORT,
    SPARK_APP_NAME,
    SPARK_JARS_PATH,
    TRADES_CHECKPOINT_DIR,
    TRADES_TRIGGER_INTERVAL,
    WATERMARK_DELAY,
    WINDOW_DURATION,
)


# =============================================================================
# CONFIGURATION
# =============================================================================

# Define the schema for incoming stock trade data
# Explicit schemas are CRITICAL in streaming because Spark can't infer schema from streams
STOCK_TRADE_SCHEMA = StructType([
    StructField("trade_id", StringType(), True),
    StructField("symbol", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("trade_type", StringType(), True),
    StructField("timestamp", StringType(), True)  # Will be converted to TimestampType
])


# =============================================================================
# SINK FUNCTIONS
# =============================================================================

def write_trades_to_postgres(batch_df, batch_id):
    """
    Write raw trade data to PostgreSQL.
    
    This function is called by foreachBatch for each micro-batch.
    The batch_id is useful for:
    - Idempotency: You can use it to avoid duplicate writes on retries
    - Debugging: Track which batch caused issues
    
    Args:
        batch_df: A regular DataFrame containing the micro-batch data
        batch_id: Unique identifier for this micro-batch
    """
    if batch_df.isEmpty():
        print(f"Batch {batch_id}: No data to write")
        return
    
    record_count = batch_df.count()
    print(f"Batch {batch_id}: Writing {record_count} trades to PostgreSQL")
    
    try:
        (batch_df.write
            .format("jdbc")
            .option("url", POSTGRES_CONFIG["url"])
            .option("dbtable", "stock_trades")
            .option("user", POSTGRES_CONFIG["user"])
            .option("password", POSTGRES_CONFIG["password"])
            .option("driver", POSTGRES_CONFIG["driver"])
            .mode("append")
            .save())
        
        print(f"Batch {batch_id}: Successfully wrote {record_count} trades")
    except Exception as e:
        print(f"Batch {batch_id}: Error writing to PostgreSQL: {e}")
        raise


def write_aggregates_to_postgres(batch_df, batch_id):
    """
    Write aggregated data to PostgreSQL.
    
    For aggregates, we rely on append-only output, which writes
    final window results once they pass the watermark.
    """
    if batch_df.isEmpty():
        print(f"Aggregate Batch {batch_id}: No aggregates to write")
        return
    
    record_count = batch_df.count()
    print(f"Aggregate Batch {batch_id}: Writing {record_count} aggregates")
    
    try:
        # Flatten the window struct for PostgreSQL
        flattened_df = (batch_df
            .withColumn("window_start", col("window.start"))
            .withColumn("window_end", col("window.end"))
            .drop("window"))
        
        (flattened_df.write
            .format("jdbc")
            .option("url", POSTGRES_CONFIG["url"])
            .option("dbtable", "stock_aggregates")
            .option("user", POSTGRES_CONFIG["user"])
            .option("password", POSTGRES_CONFIG["password"])
            .option("driver", POSTGRES_CONFIG["driver"])
            .mode("append")
            .save())
        
        print(f"Aggregate Batch {batch_id}: Successfully wrote aggregates")
    except Exception as e:
        print(f"Aggregate Batch {batch_id}: Error: {e}")
        raise


# =============================================================================
# SOURCE READERS
# =============================================================================

def create_socket_stream(spark):
    """
    Create a streaming DataFrame from a TCP socket.
    
    Socket streaming is great for development because:
    - Easy to set up (just need netcat or a Python socket server)
    - Low latency for testing
    - Visual feedback as you send data
    
    Limitations (not for production):
    - No fault tolerance (lost connection = lost data)
    - Single receiver (no parallelism)
    - No replay capability
    """
    print(f"Creating socket stream source (host: {SOCKET_HOST}, port: {SOCKET_PORT})")
    
    raw_stream = (spark.readStream
        .format("socket")
        .option("host", SOCKET_HOST)
        .option("port", SOCKET_PORT)
        .load())
    
    # Socket source gives us a single "value" column containing the raw text
    # We need to parse it as JSON and apply our schema
    parsed_stream = (raw_stream
        .select(from_json(col("value"), STOCK_TRADE_SCHEMA).alias("data"))
        .select("data.*")
        .withColumn("timestamp", to_timestamp(col("timestamp"))))
    
    return parsed_stream


def create_file_stream(spark):
    """
    Create a streaming DataFrame from a directory of Parquet files.
    
    File streaming is useful because:
    - Fault tolerant (files persist)
    - Can handle large volumes
    - Works well with cloud storage (S3, GCS, ADLS)
    
    How it works:
    - Spark watches the directory for new files
    - Each new file triggers a micro-batch
    - Files are processed exactly once (tracked via checkpoint)
    """
    print(f"Creating file stream source (watching {FILE_INPUT_DIR} for Parquet files)")
    
    # For file sources, we CAN provide schema directly in the read
    file_schema = StructType([
        StructField("trade_id", StringType(), True),
        StructField("symbol", StringType(), True),
        StructField("price", DoubleType(), True),
        StructField("quantity", IntegerType(), True),
        StructField("trade_type", StringType(), True),
        StructField("timestamp", TimestampType(), True)
    ])
    
    file_stream = (spark.readStream
        .format("parquet")
        .schema(file_schema)
        .option("path", FILE_INPUT_DIR)
        .option("maxFilesPerTrigger", FILE_MAX_FILES_PER_TRIGGER)  # Process one file per batch (good for learning)
        .load())
    
    return file_stream


def create_rate_stream(spark):
    """
    Create a streaming DataFrame using Spark's built-in rate source.
    
    The rate source is perfect for:
    - Testing without external dependencies
    - Benchmarking throughput
    - Learning Spark Streaming basics
    
    It generates rows with:
    - timestamp: when the row was generated
    - value: monotonically increasing counter
    
    We'll transform this into fake stock data for consistency.
    """
    print(f"Creating rate stream source ({RATE_ROWS_PER_SECOND} rows per second)")
    
    rate_stream = (spark.readStream
        .format("rate")
        .option("rowsPerSecond", RATE_ROWS_PER_SECOND)
        .option("numPartitions", RATE_NUM_PARTITIONS)
        .load())
    
    # Transform rate data into stock-like data
    # This demonstrates how to enrich simple data with derived columns
    transformed_stream = (rate_stream
        .withColumn("trade_id", expr("concat('RATE-', value)"))
        .withColumn(
            "symbol",
            expr(
                "element_at("
                f"array{tuple(RATE_SYMBOLS)}, "
                f"cast((value % {RATE_SYMBOL_MOD}) + 1 as int))"
            ),
        )
        .withColumn("price", expr("100.0 + (value % 100) + (rand() * 10)"))
        .withColumn("quantity", expr("cast((rand() * 1000) + 1 as int)"))
        .withColumn("trade_type", expr("case when rand() > 0.5 then 'BUY' else 'SELL' end"))
        .drop("value"))
    
    return transformed_stream


# =============================================================================
# TRANSFORMATIONS
# =============================================================================

def enrich_trades(df):
    """
    Add derived columns to the trade data.
    
    This demonstrates common streaming transformations:
    - Calculated fields (trade_value)
    - Conditional logic (price_category)
    - Adding processing metadata
    """
    enriched_df = (df
        .withColumn("trade_value", col("price") * col("quantity"))
        .withColumn("price_category",
            when(col("price") > 200, "very_high")
            .when(col("price") > 150, "high")
            .when(col("price") > 100, "medium")
            .otherwise("low")
        ))
    
    return enriched_df


def create_aggregations(df):
    """
    Create windowed aggregations on the streaming data.
    
    Key concepts demonstrated:
    
    1. Watermarking: Tells Spark how late data can arrive
       - Data arriving more than 2 minutes late will be dropped
       - Enables Spark to clean up old state
    
    2. Window Function: Groups data into time buckets
       - "1 minute" = tumbling window (non-overlapping)
       - Can also do sliding windows: window(col, "5 minutes", "1 minute")
    
    3. Aggregation Functions: Standard SQL aggregates work in streaming
    """
    aggregated_df = (df
        .withWatermark("timestamp", WATERMARK_DELAY)
        .groupBy(
            window(col("timestamp"), WINDOW_DURATION),
            col("symbol")
        )
        .agg(
            avg("price").alias("avg_price"),
            min("price").alias("min_price"),
            max("price").alias("max_price"),
            sum("quantity").alias("total_volume"),
            count("*").alias("trade_count"),
            sum("trade_value").alias("total_value")
        ))
    
    return aggregated_df


# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main(source_type="socket"):
    """
    Main entry point for the streaming application.
    
    Args:
        source_type: One of "socket", "file", or "rate"
    """
    print("=" * 60)
    print("SPARK STRUCTURED STREAMING - STOCK TRADE PROCESSOR")
    print(f"Source Type: {source_type}")
    print("=" * 60)
    
    # Create Spark Session
    # Note: In cluster mode, most config comes from spark-submit
    spark = (SparkSession.builder
        .appName(SPARK_APP_NAME)
        .config("spark.sql.streaming.checkpointLocation", CHECKPOINT_BASE_DIR)
        .config("spark.jars", SPARK_JARS_PATH)
        .getOrCreate())
    
    # Set log level to reduce noise (optional)
    spark.sparkContext.setLogLevel("WARN")
    
    print(f"Spark Session created. App ID: {spark.sparkContext.applicationId}")
    print(f"Spark UI available at: http://localhost:4040")
    
    # Create the appropriate stream source
    if source_type == "socket":
        raw_stream = create_socket_stream(spark)
    elif source_type == "file":
        raw_stream = create_file_stream(spark)
    elif source_type == "rate":
        raw_stream = create_rate_stream(spark)
    else:
        raise ValueError(f"Unknown source type: {source_type}. Use: socket, file, or rate")
    
    # Apply transformations
    enriched_stream = enrich_trades(raw_stream)
    
    # Create aggregated stream
    aggregated_stream = create_aggregations(enriched_stream)
    
    # ==========================================================================
    # OUTPUT STREAMS
    # ==========================================================================
    
    # Stream 1: Write raw (enriched) trades to PostgreSQL
    trades_query = (enriched_stream.writeStream
        .foreachBatch(write_trades_to_postgres)
        .outputMode("append")
        .trigger(processingTime=TRADES_TRIGGER_INTERVAL)
        .queryName("trades_to_postgres")
        .option("checkpointLocation", TRADES_CHECKPOINT_DIR)
        .start())
    
    # Stream 2: Write aggregates to PostgreSQL
    # Note: Using "append" mode to write finalized window results only
    aggregates_query = (aggregated_stream.writeStream
        .foreachBatch(write_aggregates_to_postgres)
        .outputMode("append")
        .trigger(processingTime=AGGREGATES_TRIGGER_INTERVAL)
        .queryName("aggregates_to_postgres")
        .option("checkpointLocation", AGG_CHECKPOINT_DIR)
        .start())
    
    # Stream 3: Console output for debugging (optional, useful for learning)
    console_query = (enriched_stream.writeStream
        .format("console")
        .outputMode("append")
        .trigger(processingTime=CONSOLE_TRIGGER_INTERVAL)
        .option("truncate", "false")
        .option("numRows", 5)
        .queryName("console_debug")
        .start())
    
    print("\n" + "=" * 60)
    print("STREAMING QUERIES STARTED")
    print("=" * 60)
    print(f"Active queries: {[q.name for q in spark.streams.active]}")
    print("\nPress Ctrl+C to stop")
    print("=" * 60 + "\n")
    
    # Wait for termination
    # In production, you'd typically use awaitAnyTermination()
    try:
        spark.streams.awaitAnyTermination()
    except KeyboardInterrupt:
        print("\nShutting down streaming queries...")
        for query in spark.streams.active:
            query.stop()
        print("All queries stopped. Goodbye!")


if __name__ == "__main__":
    # Get source type from command line argument
    source_type = sys.argv[1] if len(sys.argv) > 1 else "socket"
    main(source_type)
