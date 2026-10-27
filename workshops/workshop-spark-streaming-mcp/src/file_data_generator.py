"""
File-based Data Generator for Spark Streaming

This script generates Parquet files containing stock trade data and places them
in a watched directory. Spark's file streaming source will automatically
pick up new files and process them.

This pattern is common in real-world scenarios where:
- Data arrives as files from external systems (FTP, S3, etc.)
- Batch data needs to be processed as a stream
- You need fault tolerance (files persist)

Usage:
    python3 file_data_generator.py [--interval SECONDS] [--trades-per-file N]

Each Parquet file contains a batch of trades.
"""

import os
import time
import random
import argparse
import uuid
from datetime import datetime

import pyarrow as pa
import pyarrow.parquet as pq

from config import (
    DEFAULT_INTERVAL_SECONDS,
    DEFAULT_MAX_FILES,
    DEFAULT_TRADES_PER_FILE,
    FILE_EXTENSION,
    FILE_PREFIX,
    OUTPUT_DIR,
    STOCKS,
    TEMP_EXTENSION,
)

# Track current prices for realistic price movements
current_prices = {symbol: info['base_price'] for symbol, info in STOCKS.items()}


# =============================================================================
# DATA GENERATION
# =============================================================================

def update_price(symbol):
    """Update price with random walk."""
    global current_prices
    
    volatility = STOCKS[symbol]['volatility']
    change = current_prices[symbol] * random.gauss(0, volatility)
    current_prices[symbol] = max(1.0, current_prices[symbol] + change)
    
    return round(current_prices[symbol], 2)


def generate_trade():
    """Generate a single trade record."""
    symbol = random.choice(list(STOCKS.keys()))
    price = update_price(symbol)
    
    # Realistic quantity distribution
    quantity = random.choices(
        [random.randint(1, 100), random.randint(100, 500), random.randint(500, 5000)],
        weights=[0.7, 0.2, 0.1]
    )[0]
    
    return {
        'trade_id': f"FILE-{uuid.uuid4().hex[:10]}",
        'symbol': symbol,
        'price': price,
        'quantity': quantity,
        'trade_type': random.choice(['BUY', 'SELL']),
        'timestamp': datetime.now()
    }


def generate_parquet_file(trades_per_file, file_number):
    """
    Generate a Parquet file with trade data.
    
    File naming is important for Spark file streaming:
    - Spark processes files in lexicographical order by default
    - Using timestamps ensures chronological processing
    - Completed files should be written atomically (write to temp, then rename)
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{FILE_PREFIX}_{timestamp}_{file_number:04d}{FILE_EXTENSION}"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Generate trades
    trades = [generate_trade() for _ in range(trades_per_file)]
    
    # Write to temporary file first, then rename (atomic write)
    # This prevents Spark from reading partially written files
    temp_filepath = filepath + TEMP_EXTENSION

    table = pa.Table.from_pylist(trades)
    pq.write_table(table, temp_filepath)
    
    # Atomic rename
    os.rename(temp_filepath, filepath)
    
    return filename, len(trades)


def cleanup_old_files(max_files=DEFAULT_MAX_FILES):
    """
    Remove old files to prevent disk space issues.
    
    In production, you'd typically:
    - Move processed files to archive
    - Use cloud storage with lifecycle policies
    - Configure Spark to clean up after processing
    """
    files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.endswith(FILE_EXTENSION)])
    
    while len(files) > max_files:
        old_file = files.pop(0)
        os.remove(os.path.join(OUTPUT_DIR, old_file))
        print(f"  Cleaned up old file: {old_file}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='File-based Trade Data Generator')
    parser.add_argument('--interval', type=int, default=DEFAULT_INTERVAL_SECONDS,
                        help=f'Seconds between file generation (default: {DEFAULT_INTERVAL_SECONDS})')
    parser.add_argument('--trades-per-file', type=int, default=DEFAULT_TRADES_PER_FILE,
                        help=f'Number of trades per file (default: {DEFAULT_TRADES_PER_FILE})')
    parser.add_argument('--max-files', type=int, default=DEFAULT_MAX_FILES,
                        help=f'Maximum files to keep (default: {DEFAULT_MAX_FILES})')
    
    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 60)
    print("FILE-BASED TRADE DATA GENERATOR")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Interval: {args.interval} seconds")
    print(f"Trades per file: {args.trades_per_file}")
    print("\nGenerating files... Press Ctrl+C to stop")
    print("=" * 60 + "\n")
    
    file_count = 0
    total_trades = 0
    
    try:
        while True:
            # Generate new file
            filename, trade_count = generate_parquet_file(args.trades_per_file, file_count)
            file_count += 1
            total_trades += trade_count
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                  f"Created: {filename} ({trade_count} trades) | "
                  f"Total files: {file_count} | Total trades: {total_trades}")
            
            # Cleanup old files
            cleanup_old_files(args.max_files)
            
            # Wait for next interval
            time.sleep(args.interval)
            
    except KeyboardInterrupt:
        print(f"\n\nStopped. Generated {file_count} files with {total_trades} total trades.")


if __name__ == "__main__":
    main()
