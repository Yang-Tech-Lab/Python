"""
AssetSentinel Pro: Industrial-Grade Signal Orchestrator
------------------------------------------------------
A high-fidelity monitoring engine designed for real-time asset 
tracking with algorithmic alert throttling and audit persistence.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Fintech Automation / Financial Intelligence
Date: March 2026
"""

import time
import random
import logging
from datetime import datetime, timedelta
from pathlib import Path
from dataclasses import dataclass
from typing import Final, Optional

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("market_intelligence.log"),
        logging.StreamHandler()
    ]
)

@dataclass
class MarketSignal:
    ticker: str
    price: float
    threshold: float
    is_breached: bool
    timestamp: str

class AssetSentinel:
    def __init__(self, ticker: str, floor_price: float):
        self.ticker: Final[str] = ticker
        self.floor_price: Final[float] = floor_price
        self.alert_cooldown: Final[int] = 300  # 5-minute cooldown (300s)
        self.last_alert_time: Optional[datetime] = None
        self.audit_trail: Final[Path] = Path("financial_audit.csv")
        
        self._initialize_audit_layer()

    def _initialize_audit_layer(self):
        """Ensures the persistence layer is provisioned with headers."""
        if not self.audit_trail.exists():
            with open(self.audit_trail, "w", encoding="utf-8") as f:
                f.write("Timestamp,Ticker,Price,Threshold,Status\n")

    def _get_market_snapshot(self) -> float:
        """
        Simulates high-fidelity market data ingestion.
        Replace with 'requests.get()' to Binance or Polygon.io in production.
        """
        # Logic: Simulated volatility around the BTC 100k psychological barrier
        return round(random.uniform(94000, 106000), 2)

    def _dispatch_notification(self, signal: MarketSignal):
        """Executes the notification protocol with throttling logic."""
        now = datetime.now()
        
        # Check if system is within the cooldown window
        if self.last_alert_time and (now - self.last_alert_time).total_seconds() < self.alert_cooldown:
            logging.info(f"⏳ Alert suppressed: Cooldown active for {self.ticker}.")
            return

        # Execute visual and file-based alert
        logging.warning(f"🚨 SIGNAL BREACH: {signal.ticker} @ ${signal.price:,.2f} (Floor: ${signal.threshold:,.2f})")
        
        with open(self.audit_trail, "a", encoding="utf-8") as f:
            f.write(f"{signal.timestamp},{signal.ticker},{signal.price},{signal.threshold},CRITICAL\n")
        
        self.last_alert_time = now

    def execute_intelligence_cycle(self):
        """Orchestrates a single monitoring pulse."""
        logging.info(f"🔍 Monitoring Node: {self.ticker} | Target Floor: ${self.floor_price:,.2f}")
        
        current_price = self._get_market_snapshot()
        is_breached = current_price < self.floor_price
        
        signal = MarketSignal(
            ticker=self.ticker,
            price=current_price,
            threshold=self.floor_price,
            is_breached=is_breached,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        if signal.is_breached:
            self._dispatch_notification(signal)
        else:
            logging.info(f"✅ Market Stability Confirmed: ${current_price:,.2f}")

if __name__ == "__main__":
    # Standard Operating Procedure (SOP)
    # Example: BTC price floor at $98,500
    sentinel = AssetSentinel(ticker="BTC-USD", floor_price=98500.00)
    
    print("\n--- Sentinel Core: Monitoring Sequence Online ---")
    try:
        # Running a simulated 5-cycle scan
        for cycle in range(1, 6):
            logging.info(f"Cycle {cycle}/5 in progress...")
            sentinel.execute_intelligence_cycle()
            time.sleep(1.5)  # Scan frequency throttling
    except KeyboardInterrupt:
        logging.info("System manually decommissioned.")
    
    print("--- Session Persisted to Audit Trail ---")
