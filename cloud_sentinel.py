"""
AssetSentinel Pro: Automated Crypto/Stock Threshold Monitor
-----------------------------------------------------------
A lightweight monitoring engine that tracks asset prices and triggers 
automated alerts when thresholds are breached.

Author: Yang Jiacheng (Yang-Tech-Lab)
License: MIT
"""

import random
import logging
from datetime import datetime
from typing import Final

# Configure professional logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class AssetMonitor:
    def __init__(self, ticker: str, threshold: float):
        self.ticker: str = ticker
        self.threshold: float = threshold
        self.log_file: Final[str] = "alert_history.log"

    def fetch_market_price(self) -> float:
        """
        Simulates fetching real-time market data.
        In production, replace with CCXT or Yahoo Finance API.
        """
        # Simulated volatility for BTC-style assets
        return round(random.uniform(95000, 105000), 2)

    def trigger_alert(self, current_price: float):
        """Executes alert sequence and logs critical data."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert_msg = f"CRITICAL: {self.ticker} dropped to ${current_price:,.2f} (Threshold: ${self.threshold:,.2f})"
        
        logging.warning(f"🚨 {alert_msg}")
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {alert_msg}\n")

    def execute_check(self):
        """Main execution flow for price monitoring."""
        logging.info(f"🔍 Monitoring Asset: {self.ticker}")
        
        current_price = self.fetch_market_price()
        logging.info(f"Current Market Price: ${current_price:,.2f}")

        if current_price < self.threshold:
            self.trigger_alert(current_price)
        else:
            logging.info("✅ Price remains within safe operational limits.")

if __name__ == "__main__":
    # Configuration: Asset Ticker and Price Floor
    # Example: BTC-USD with a $98,000 alert floor
    monitor = AssetMonitor(ticker="BTC-USD", threshold=98000.00)
    
    print("--- Sentinel Protocol Initiated ---")
    monitor.execute_check()
    print("--- Session Complete ---")
