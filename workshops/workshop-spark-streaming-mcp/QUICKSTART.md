# Quick Start Guide

This project is a hands-on path to learn Spark Structured Streaming with a
realistic pipeline: streaming sources → Spark transforms → Postgres storage →
MCP queries. The goal is to see data flow end-to-end and understand where each
piece fits.

Recommended path (fastest to validate):
1) Rate source (no generator) → 2) Socket source → 3) Query Postgres → 4) MCP

This guide gets the project running end-to-end. Follow the steps in order to
avoid setup drift.

## Step-by-Step Instructions for M4 Mac with Colima

### Prerequisites Check
Why: confirm local tooling before you build containers to avoid ambiguous
Docker/Colima errors.

```bash
# Verify Colima is installed
colima version

# Verify Docker CLI is installed
docker --version

# Verify docker-compose is available (or docker compose)
docker-compose version
```

### Step 1: Start Colima with Adequate Resources
Why: Spark needs CPU and memory headroom or jobs will fail or be very slow.
Allocate at least 4 CPUs and 8GB RAM:

```bash
# If Colima is already running, stop it first
colima stop

# Start with recommended resources for Spark
colima start --cpu 4 --memory 8 --disk 60

# Verify it's running
colima status
```

### Step 2: Navigate to Project and Build
Why: this builds the unified image (Python 3.12+, Spark 4.0.1, Java 21) and
starts Spark, Postgres, and the MCP server.

```bash
# Navigate to the project directory
cd spark-streaming-project

# Build and start all containers
docker-compose up -d --build

# This will:
# 1. Build the custom Spark image with PostgreSQL driver
# 2. Start PostgreSQL (initializes schema automatically)
# 3. Start Spark Master
# 4. Start Spark Worker

# Wait for all containers to be healthy (about 30 seconds)
docker-compose ps

# You should see all containers as "Up" or "healthy"
```

### Step 3: Verify Setup
Why: confirm each service is healthy before starting streaming jobs.

```bash
# Check Spark Master logs
docker-compose logs spark-master

# Check Spark Worker connected
docker-compose logs spark-worker

# Verify PostgreSQL is ready
docker-compose exec postgres psql -U sparkuser -d sparkdb -c "SELECT 'Database ready!' as status;"
```

### Step 4: Run with Rate Source (Easiest - No Generator Needed)
Why: the fastest sanity check. Spark generates data internally, so there is no
external dependency.

```bash
# Start the streaming processor with rate source
docker-compose exec spark-master spark-submit \
    --master spark://spark-master:7077 \
    --driver-class-path /opt/spark/jars/postgresql-42.7.1.jar \
    --conf spark.executor.extraClassPath=/opt/spark/jars/postgresql-42.7.1.jar \
    /app/src/stream_processor.py rate
```

### Step 5: Run with Socket Source (More Realistic)
Why: this simulates a real-time feed over a TCP socket.

Open TWO terminals:

**Terminal 1 - Start Data Generator:**
```bash
docker-compose exec spark-master python3 /app/src/stock_data_generator.py --rate 5
```

**Terminal 2 - Start Streaming Processor:**
```bash
docker-compose exec spark-master spark-submit \
    --master spark://spark-master:7077 \
    --driver-class-path /opt/spark/jars/postgresql-42.7.1.jar \
    --conf spark.executor.extraClassPath=/opt/spark/jars/postgresql-42.7.1.jar \
    /app/src/stream_processor.py socket
```

### Step 6: Optional - File Source (Not Working Yet)
Why: file streaming is a common pattern, but this path is currently unstable.
Use Rate or Socket sources for now.

Open TWO terminals (optional):

**Terminal 1 - Start File Generator:**
```bash
docker-compose exec spark-master python3 /app/src/file_data_generator.py --interval 10
```

**Terminal 2 - Start Streaming Processor:**
```bash
docker-compose exec spark-master spark-submit \
    --master spark://spark-master:7077 \
    --driver-class-path /opt/spark/jars/postgresql-42.7.1.jar \
    --conf spark.executor.extraClassPath=/opt/spark/jars/postgresql-42.7.1.jar \
    /app/src/stream_processor.py file
```

### Step 7: Query the Database
Why: verify that streaming data was written to Postgres and aggregates exist.

Open a new terminal:

```bash
# Connect to PostgreSQL
docker-compose exec postgres psql -U sparkuser -d sparkdb

# Once connected, try these queries:

# View recent trades
SELECT * FROM stock_trades ORDER BY timestamp DESC LIMIT 10;

# Count total trades
SELECT COUNT(*) FROM stock_trades;

# View aggregations
SELECT * FROM stock_aggregates ORDER BY window_start DESC LIMIT 10;

# View by symbol
SELECT symbol, COUNT(*) as trades, AVG(price) as avg_price 
FROM stock_trades 
GROUP BY symbol 
ORDER BY trades DESC;

# Watch data arrive in real-time (updates every 2 seconds)
\watch SELECT COUNT(*) as total, MAX(timestamp) as latest FROM stock_trades;

# Exit PostgreSQL
\q
```

### Step 8: Connect to the MCP Server
Why: MCP lets you query and summarize the streaming tables without custom SQL.

The MCP server runs alongside Spark and Postgres and exposes read-only tools
for querying `stock_trades` and `stock_aggregates`.

```bash
# Tail MCP server logs
docker-compose logs -f mcp-server
```

Note: The Docker image uses Python 3.12+, Spark 4.0.1, and Java 21 for all
services to avoid version mismatches across Spark and MCP.
The image entrypoint is the MCP server, so Spark services override the entrypoint
in `docker-compose.yml`.

Connect using any MCP client over SSE:
- Endpoint: `http://localhost:3333/sse`
- Tools: `latest_prices`, `recent_trades`, `window_aggregates`, `symbol_summary`

If you use MCP Inspector:
```bash
npx @modelcontextprotocol/inspector http://localhost:3333/sse
```
Then connect to the SSE endpoint in your browser and monitor with:
```bash
docker-compose logs -f mcp-server
```

### Step 9: Monitor via Web UI
Why: optional visibility into running Spark jobs and cluster state.

Open your browser to:
- **Spark Master UI**: http://localhost:8080
- **Spark Application UI** (when job running): http://localhost:4040

### Step 10: Cleanup
Why: stop resources and reset the environment cleanly.

```bash
# Stop streaming job: Press Ctrl+C in the terminal running spark-submit

# Stop data generator: Press Ctrl+C in the terminal running the generator

# Stop all containers
docker-compose down

# Stop and remove all data (fresh start)
docker-compose down -v

# Stop Colima when done
colima stop
```

## Troubleshooting

### "Cannot connect to Docker daemon"
```bash
colima status  # Check if running
colima start   # Start if not running
```

### "Port already in use"
```bash
# Check what's using the port
lsof -i :8080
lsof -i :5432

# Kill the process or change ports in docker-compose.yml
```

### "Out of memory"
```bash
# Restart Colima with more memory
colima stop
colima start --cpu 4 --memory 10
```

### "No data in database"
1. Check generator is running
2. Check Spark logs: `docker-compose logs spark-master`
3. Verify network: `docker-compose exec spark-master ping postgres`

### "Driver class not found"
Make sure you're using the correct spark-submit options with the JDBC driver paths.
