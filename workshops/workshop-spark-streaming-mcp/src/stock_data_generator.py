"""
Stock Data Generator for Spark Streaming

This script generates realistic stock trade data and sends it to a socket.
It can operate in two modes:

1. GENERATED MODE (default): Creates synthetic but realistic stock data
   - Uses realistic price movements (random walk with drift)
   - Simulates market hours patterns
   - Includes multiple stock symbols

2. ONLINE MODE: Fetches real data from public APIs
   - Uses free APIs when available
   - Falls back to generated data if API fails

Usage:
    python3 stock_data_generator.py [--online] [--rate TRADES_PER_SECOND]

The generator sends JSON messages over a TCP socket (port 9999).
"""

import socket
import json
import time
import random
import argparse
from datetime import datetime
import threading
import uuid

# Try to import optional dependencies
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Warning: 'requests' not installed. Online mode disabled.")


# =============================================================================
# CONFIGURATION
# =============================================================================

# Socket configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 9999

# Stock symbols to simulate
STOCK_SYMBOLS = {
    'AAPL': {'name': 'Apple Inc.', 'base_price': 175.0, 'volatility': 0.02},
    'GOOGL': {'name': 'Alphabet Inc.', 'base_price': 140.0, 'volatility': 0.025},
    'MSFT': {'name': 'Microsoft Corp.', 'base_price': 380.0, 'volatility': 0.018},
    'AMZN': {'name': 'Amazon.com Inc.', 'base_price': 180.0, 'volatility': 0.022},
    'META': {'name': 'Meta Platforms', 'base_price': 500.0, 'volatility': 0.03},
    'NVDA': {'name': 'NVIDIA Corp.', 'base_price': 880.0, 'volatility': 0.035},
    'TSLA': {'name': 'Tesla Inc.', 'base_price': 250.0, 'volatility': 0.04},
    'JPM': {'name': 'JPMorgan Chase', 'base_price': 195.0, 'volatility': 0.015},
}

# Current prices (updated with random walk)
current_prices = {symbol: info['base_price'] for symbol, info in STOCK_SYMBOLS.items()}


# =============================================================================
# DATA GENERATION
# =============================================================================

def generate_price_movement(symbol):
    """
    Generate realistic price movement using geometric Brownian motion.
    
    This simulates how real stock prices move:
    - Small random changes that compound
    - Higher volatility = larger swings
    - Prices can drift up or down over time
    """
    global current_prices
    
    stock_info = STOCK_SYMBOLS[symbol]
    volatility = stock_info['volatility']
    
    # Random walk with slight upward drift (simulating long-term market growth)
    drift = 0.0001  # Small positive drift
    random_shock = random.gauss(0, volatility)
    
    # Update price
    price_change = current_prices[symbol] * (drift + random_shock)
    current_prices[symbol] = max(1.0, current_prices[symbol] + price_change)
    
    # Round to 2 decimal places
    return round(current_prices[symbol], 2)


def generate_trade():
    """
    Generate a single synthetic trade.
    
    Returns a dictionary containing trade details that mimics
    real market data feeds.
    """
    symbol = random.choice(list(STOCK_SYMBOLS.keys()))
    price = generate_price_movement(symbol)
    
    # Generate realistic quantity distribution
    # Most trades are small, few are large (power law distribution)
    if random.random() < 0.7:
        quantity = random.randint(1, 100)  # Small retail trade
    elif random.random() < 0.9:
        quantity = random.randint(100, 1000)  # Medium institutional
    else:
        quantity = random.randint(1000, 10000)  # Large block trade
    
    trade = {
        'trade_id': str(uuid.uuid4())[:12],
        'symbol': symbol,
        'price': price,
        'quantity': quantity,
        'trade_type': random.choice(['BUY', 'SELL']),
        'timestamp': datetime.now().isoformat()
    }
    
    return trade


def fetch_online_data():
    """
    Attempt to fetch real market data from public APIs.
    
    Note: Most real-time stock APIs require authentication.
    This function tries free alternatives and falls back to generated data.
    """
    if not REQUESTS_AVAILABLE:
        return None
    
    # Try CoinGecko API for crypto prices (free, no auth required)
    # We'll use this as a proxy for "online" data
    try:
        response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price',
            params={
                'ids': 'bitcoin,ethereum,dogecoin',
                'vs_currencies': 'usd',
                'include_24hr_change': 'true'
            },
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            # Convert to our trade format
            crypto_map = {
                'bitcoin': ('BTC', data.get('bitcoin', {}).get('usd', 60000)),
                'ethereum': ('ETH', data.get('ethereum', {}).get('usd', 3000)),
                'dogecoin': ('DOGE', data.get('dogecoin', {}).get('usd', 0.1))
            }
            
            symbol, price = random.choice(list(crypto_map.values()))
            
            return {
                'trade_id': str(uuid.uuid4())[:12],
                'symbol': symbol,
                'price': round(price * (1 + random.gauss(0, 0.001)), 2),
                'quantity': random.randint(1, 100),
                'trade_type': random.choice(['BUY', 'SELL']),
                'timestamp': datetime.now().isoformat()
            }
    except Exception as e:
        print(f"Online fetch failed: {e}")
    
    return None


# =============================================================================
# SOCKET SERVER
# =============================================================================

class TradeStreamServer:
    """
    TCP Socket server that streams trade data to connected clients.
    
    In real-world scenarios, you'd use:
    - Apache Kafka for production streaming
    - AWS Kinesis or Google Pub/Sub for cloud deployments
    
    Socket streaming is used here for simplicity and learning.
    """
    
    def __init__(self, host, port, trades_per_second=5, use_online=False):
        self.host = host
        self.port = port
        self.trades_per_second = trades_per_second
        self.use_online = use_online
        self.clients = []
        self.running = False
        self.trade_count = 0
    
    def start(self):
        """Start the socket server and begin streaming data."""
        self.running = True
        
        # Create server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        server_socket.settimeout(1.0)
        
        print("=" * 60)
        print("STOCK TRADE DATA GENERATOR")
        print("=" * 60)
        print(f"Listening on {self.host}:{self.port}")
        print(f"Mode: {'Online + Generated' if self.use_online else 'Generated only'}")
        print(f"Rate: {self.trades_per_second} trades/second")
        print("\nWaiting for Spark to connect...")
        print("Press Ctrl+C to stop")
        print("=" * 60 + "\n")
        
        # Start data generation thread
        data_thread = threading.Thread(target=self._generate_and_send)
        data_thread.daemon = True
        data_thread.start()
        
        # Accept connections
        try:
            while self.running:
                try:
                    client_socket, address = server_socket.accept()
                    print(f"✓ Client connected from {address}")
                    self.clients.append(client_socket)
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.running:
                        print(f"Accept error: {e}")
        except KeyboardInterrupt:
            print("\nShutting down...")
        finally:
            self.running = False
            for client in self.clients:
                try:
                    client.close()
                except:
                    pass
            server_socket.close()
            print(f"Server stopped. Total trades sent: {self.trade_count}")
    
    def _generate_and_send(self):
        """Background thread that generates and sends trade data."""
        interval = 1.0 / self.trades_per_second
        
        while self.running:
            if not self.clients:
                time.sleep(0.1)
                continue
            
            # Generate trade (try online first if enabled)
            trade = None
            if self.use_online and random.random() < 0.3:  # 30% chance of online data
                trade = fetch_online_data()
            
            if trade is None:
                trade = generate_trade()
            
            # Convert to JSON and send
            message = json.dumps(trade) + "\n"
            
            # Send to all connected clients
            disconnected = []
            for client in self.clients:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    disconnected.append(client)
            
            # Remove disconnected clients
            for client in disconnected:
                self.clients.remove(client)
                print("Client disconnected")
            
            self.trade_count += 1
            
            # Print status every 100 trades
            if self.trade_count % 100 == 0:
                print(f"Trades sent: {self.trade_count} | "
                      f"Clients: {len(self.clients)} | "
                      f"Latest: {trade['symbol']} @ ${trade['price']}")
            
            time.sleep(interval)


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='Stock Trade Data Generator')
    parser.add_argument('--online', action='store_true',
                        help='Enable fetching from online APIs')
    parser.add_argument('--rate', type=int, default=5,
                        help='Trades per second (default: 5)')
    
    args = parser.parse_args()
    
    server = TradeStreamServer(
        host=HOST,
        port=PORT,
        trades_per_second=args.rate,
        use_online=args.online
    )
    
    server.start()


if __name__ == "__main__":
    main()
