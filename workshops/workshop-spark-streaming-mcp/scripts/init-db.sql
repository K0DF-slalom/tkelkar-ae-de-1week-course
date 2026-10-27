-- PostgreSQL Schema Initialization for Spark Streaming Project
-- This script runs automatically when the PostgreSQL container starts

-- Table for raw stock trade data
-- Each row represents a single trade event from the stream
CREATE TABLE IF NOT EXISTS stock_trades (
    id SERIAL PRIMARY KEY,
    trade_id VARCHAR(50) UNIQUE,          -- Unique identifier for each trade
    symbol VARCHAR(10) NOT NULL,           -- Stock ticker symbol (e.g., AAPL, GOOGL)
    price DECIMAL(10, 2) NOT NULL,         -- Trade price
    quantity INTEGER NOT NULL,             -- Number of shares traded
    trade_value DECIMAL(15, 2),            -- Calculated: price * quantity
    price_category VARCHAR(20),            -- Derived: high/medium/low based on price
    trade_type VARCHAR(10),                -- BUY or SELL
    timestamp TIMESTAMP NOT NULL,          -- When the trade occurred
    processed_at TIMESTAMP DEFAULT NOW()   -- When Spark processed this record
);

-- Index for efficient time-based queries
-- This is crucial for streaming analytics where you often query recent data
CREATE INDEX IF NOT EXISTS idx_stock_trades_timestamp ON stock_trades(timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_stock_trades_symbol ON stock_trades(symbol);

-- Table for windowed aggregations
-- Stores pre-computed statistics per time window and symbol
CREATE TABLE IF NOT EXISTS stock_aggregates (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    window_start TIMESTAMP NOT NULL,
    window_end TIMESTAMP NOT NULL,
    avg_price DECIMAL(10, 2),
    min_price DECIMAL(10, 2),
    max_price DECIMAL(10, 2),
    total_volume BIGINT,                   -- Sum of all quantities in window
    trade_count INTEGER,                   -- Number of trades in window
    total_value DECIMAL(20, 2),            -- Sum of all trade values in window
    processed_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(symbol, window_start, window_end)  -- Prevent duplicate windows
);

-- Index for efficient aggregate queries
CREATE INDEX IF NOT EXISTS idx_stock_aggregates_window ON stock_aggregates(window_start DESC);
CREATE INDEX IF NOT EXISTS idx_stock_aggregates_symbol ON stock_aggregates(symbol);

-- Table for rate source data (for testing with Spark's built-in rate source)
CREATE TABLE IF NOT EXISTS rate_events (
    id SERIAL PRIMARY KEY,
    event_timestamp TIMESTAMP NOT NULL,
    event_value BIGINT NOT NULL,
    processed_at TIMESTAMP DEFAULT NOW()
);

-- View for easy analysis: latest price per symbol
CREATE OR REPLACE VIEW latest_prices AS
SELECT DISTINCT ON (symbol)
    symbol,
    price as latest_price,
    timestamp as last_trade_time,
    trade_type
FROM stock_trades
ORDER BY symbol, timestamp DESC;

-- View for daily trading summary
CREATE OR REPLACE VIEW daily_summary AS
SELECT 
    symbol,
    DATE(timestamp) as trade_date,
    COUNT(*) as trade_count,
    SUM(quantity) as total_volume,
    SUM(trade_value) as total_value,
    AVG(price) as avg_price,
    MIN(price) as min_price,
    MAX(price) as max_price
FROM stock_trades
GROUP BY symbol, DATE(timestamp)
ORDER BY trade_date DESC, symbol;

-- Helpful function to clean up old data (useful during development)
CREATE OR REPLACE FUNCTION cleanup_old_data(days_to_keep INTEGER DEFAULT 7)
RETURNS void AS $$
BEGIN
    DELETE FROM stock_trades WHERE timestamp < NOW() - (days_to_keep || ' days')::INTERVAL;
    DELETE FROM stock_aggregates WHERE window_start < NOW() - (days_to_keep || ' days')::INTERVAL;
    DELETE FROM rate_events WHERE event_timestamp < NOW() - (days_to_keep || ' days')::INTERVAL;
END;
$$ LANGUAGE plpgsql;

-- Grant permissions (in case you need to connect with different users)
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sparkuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO sparkuser;

-- Print confirmation
DO $$
BEGIN
    RAISE NOTICE 'Database schema initialized successfully!';
    RAISE NOTICE 'Tables created: stock_trades, stock_aggregates, rate_events';
    RAISE NOTICE 'Views created: latest_prices, daily_summary';
END $$;
