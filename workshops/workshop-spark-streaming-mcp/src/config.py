"""Shared configuration constants for the streaming app."""

# PostgreSQL connection settings
POSTGRES_CONFIG = {
    "url": "jdbc:postgresql://postgres:5432/sparkdb",
    "user": "sparkuser",
    "password": "sparkpass",
    "driver": "org.postgresql.Driver",
}

# Spark streaming app settings
SPARK_APP_NAME = "StockTradeStreaming"
SPARK_JARS_PATH = "/opt/spark/jars/postgresql-42.7.1.jar"
CHECKPOINT_BASE_DIR = "/tmp/spark-checkpoints"
TRADES_CHECKPOINT_DIR = f"{CHECKPOINT_BASE_DIR}/trades"
AGG_CHECKPOINT_DIR = f"{CHECKPOINT_BASE_DIR}/aggregates"

TRADES_TRIGGER_INTERVAL = "10 seconds"
AGGREGATES_TRIGGER_INTERVAL = "30 seconds"
CONSOLE_TRIGGER_INTERVAL = "15 seconds"

# Socket source settings
SOCKET_HOST = "spark-master"
SOCKET_PORT = 9999

# File source settings
FILE_INPUT_DIR = "/app/data/input"
FILE_MAX_FILES_PER_TRIGGER = 1

# Rate source settings
RATE_ROWS_PER_SECOND = 10
RATE_NUM_PARTITIONS = 2
RATE_SYMBOLS = ["AAPL", "GOOGL", "MSFT", "AMZN", "META"]
RATE_SYMBOL_MOD = len(RATE_SYMBOLS)

# Aggregation settings
WATERMARK_DELAY = "2 minutes"
WINDOW_DURATION = "1 minute"

# File generator settings
OUTPUT_DIR = FILE_INPUT_DIR
DEFAULT_INTERVAL_SECONDS = 10
DEFAULT_TRADES_PER_FILE = 50
DEFAULT_MAX_FILES = 50
FILE_PREFIX = "trades"
FILE_EXTENSION = ".parquet"
TEMP_EXTENSION = ".tmp"

# Stock symbols and their characteristics for file generation
STOCKS = {
    "AAPL": {"base_price": 175.0, "volatility": 0.02},
    "GOOGL": {"base_price": 140.0, "volatility": 0.025},
    "MSFT": {"base_price": 380.0, "volatility": 0.018},
    "AMZN": {"base_price": 180.0, "volatility": 0.022},
    "META": {"base_price": 500.0, "volatility": 0.03},
    "NVDA": {"base_price": 880.0, "volatility": 0.035},
    "TSLA": {"base_price": 250.0, "volatility": 0.04},
}
