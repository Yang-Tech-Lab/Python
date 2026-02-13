"""
MarketIntel-Sim: Advanced Synthetic Market Data Generator
---------------------------------------------------------
A modular simulation engine designed to synthesize multi-day market pricing 
volatility for competitive intelligence testing.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Synthesis / Market Intelligence
Date: February 2026
"""

import pandas as pd
import random
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Final

# 1. Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class MarketSimulator:
    def __init__(self, simulation_days: int = 7):
        self.simulation_days: int = simulation_days
        self.output_file: Final[str] = "competitor_data.csv"
        
        # Defining professional-grade hardware assets for simulation
        #
        self.inventory_matrix: Dict[str, float] = {
            "ESP32-S3 DevKit": 15.00,
            "Logic Analyzer Pro": 120.00,
            "USB-C Oscilloscope": 250.00,
            "Mechanical Macro Pad": 45.00,
            "4K Field Monitor": 180.00
        }

    def _calculate_volatility(self, base_price: float) -> float:
        """Applies a Gaussian-style volatility factor to the base price."""
        # Using a variance range of 0.9x to 1.1x to simulate market noise
        fluctuation = random.uniform(0.9, 1.1)
        return round(base_price * fluctuation, 2)

    def execute_simulation(self) -> List[Dict]:
        """Orchestrates the time-series data generation sequence."""
        logging.info(f"Initiating {self.simulation_days}-day market cycle simulation...")
        simulated_records = []

        for day_offset in range(self.simulation_days):
            # Calculating historical date range
            target_date = (datetime.now() - timedelta(days=self.simulation_days - 1 - day_offset)).strftime("%Y-%m-%d")
            
            for product, base_price in self.inventory_matrix.items():
                current_market_price = self._calculate_volatility(base_price)
                
                # Internal logic: COGS (Cost of Goods Sold) assumed at 60% of base
                production_cost = round(base_price * 0.6, 2)
                
                simulated_records.append({
                    "Date": target_date,
                    "Product": product,
                    "Competitor_Price": current_market_price,
                    "My_Cost": production_cost
                })
        
        return simulated_records

    def persist_to_csv(self):
        """Transforms simulated records into a persistent CSV dataset."""
        data = self.execute_simulation()
        df = pd.DataFrame(data)
        
        try:
            df.to_csv(self.output_file, index=False)
            logging.info(f"✅ Simulation Complete. Data persisted at: [{self.output_file}]")
        except Exception as e:
            logging.error(f"❌ Persistence Failure: {e}")

if __name__ == "__main__":
    # Initialize and run the simulation engine
    print("🚀 AssetSentinel: Market Data Synthesis Suite Online")
    simulator = MarketSimulator(simulation_days=7)
    simulator.persist_to_csv()
    print("-" * 50)
