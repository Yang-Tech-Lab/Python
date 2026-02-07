"""
AssetSentinel Pro: High-Frequency Automated Market Monitor
----------------------------------------------------------
A robust, asynchronous polling engine designed to track asset volatility 
and execute automated alert protocols based on user-defined thresholds.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Fintech Automation / DevOps
Date: February 2026
"""

import schedule
import time
import pandas as pd
import logging
import os
import random
from datetime import datetime
from typing import Final

# 1. Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class MarketSentinel:
    def __init__(self, ticker: str, threshold: float):
        self.ticker: str = ticker
        self.threshold: float = threshold
        self.log_file: Final[str] = "market_surveillance_log.csv"
        self._init_system()

    def _init_system(self):
        """Initializes the monitoring environment and logging headers."""
        logging.info("🛡️ AssetSentinel System Initialized (Simulation Mode).")
        logging.info(f"Targeting Asset: {self.ticker} | Alert Threshold: < ${self.threshold:,.2f}")
        
        if not os.path.exists(self.log_file):
            pd.DataFrame(columns=["Timestamp", "Asset", "Price_USD", "Status"]).to_csv(
                self.log_file, index=False, encoding='utf-8-sig'
            )

    def _fetch_simulated_price(self) -> float:
        """
        Simulates real-time market volatility. 
        In production, replace this with a WebSocket or REST API call (e.g., Binance/Yahoo Finance).
        """
        return round(random.uniform(95000, 102000), 2)

    def _persist_data(self, price: float, status: str):
        """Appends transaction data to the local ledger for audit trails."""
        entry = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Asset": self.ticker,
            "Price_USD": f"{price:.2f}",
            "Status": status
        }])
        entry.to_csv(self.log_file, mode='a', header=False, index=False, encoding='utf-8-sig')

    def _trigger_alert_protocol(self, price: float):
        """Executes emergency alert notification sequence."""
        red_code = "\033[91m"
        reset_code = "\033[0m"
        
        logging.warning(f"{red_code}CRITICAL BREACH DETECTED!{reset_code}")
        print(f"{red_code}" + "="*50)
        print(f"🚨 ALERT: {self.ticker} Price Collapse")
        print(f"📉 Current Valuation: ${price:,.2f}")
        print(f"🛑 Security Threshold: ${self.threshold:,.2f}")
        print(f"📧 Notification Status: Automated dispatch sent to Administrator.")
        print("="*50 + f"{reset_code}")

    def patrol_routine(self):
        """The core polling cycle executed by the scheduler."""
        current_price = self._fetch_simulated_price()
        status = "OK" if current_price >= self.threshold else "⚠️ ALERT"
        
        logging.info(f"Surveillance Polling: {self.ticker} at ${current_price:,.2f} -> Status: {status}")
        
        self._persist_data(current_price, status)
        
        if current_price < self.threshold:
            self._trigger_alert_protocol(current_price)

def main():
    # Configuration: BTC-USD with a $98,000 Alert Floor
    sentinel = MarketSentinel(ticker="BTC-USD", threshold=98000.0)

    # Schedule: High-frequency check every 3 seconds for demonstration
    schedule.every(3).seconds.do(sentinel.patrol_routine)

    logging.info("System Deployment Successful. Press Ctrl+C to terminate session.")
    print("-" * 60)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("System shutdown initiated by user. Terminating Sentinel protocols.")

if __name__ == "__main__":
    main()
