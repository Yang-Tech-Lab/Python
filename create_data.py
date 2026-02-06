"""
SalesData Synthesis Engine
--------------------------
A high-fidelity data generation utility designed to simulate international 
e-commerce transactions for testing automation pipelines.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Automation
"""

import pandas as pd
import logging
from typing import Dict, List

# Initialize professional logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class DataSynthesisEngine:
    def __init__(self, file_name: str = "fiverr_sales_data.xlsx"):
        self.file_name = file_name
        # Reflecting your interest in high-end tech hardware (MacBooks, etc.)
        self.raw_payload: Dict[str, List] = {
            'Order_ID': ['ORD_2026_001', 'ORD_2026_002', 'ORD_2026_003', 'ORD_2026_004', 'ORD_2026_005'],
            'Product_Line': ['iPhone 17 Pro', 'MacBook Pro M4', 'AirPods Max 2', 'iPad Ultra', 'Apple Watch Ultra 3'],
            'Unit_Price_USD': [1199, 2499, 549, 899, 799],
            'Quantity_Sold': [12, 5, 25, 8, 15],
            'Region': ['USA', 'United Kingdom', 'European Union', 'China', 'Singapore']
        }

    def generate_dataframe(self) -> pd.DataFrame:
        """Converts raw payload into a structured Pandas DataFrame."""
        logging.info("Initializing data synthesis sequence...")
        df = pd.DataFrame(self.raw_payload)
        
        # Calculate Total Revenue per line item (Feature Engineering)
        df['Total_Revenue'] = df['Unit_Price_USD'] * df['Quantity_Sold']
        return df

    def export(self):
        """Persists the synthesized data to an Excel binary."""
        try:
            df = self.generate_dataframe()
            logging.info(f"Exporting dataset to {self.file_name}...")
            
            # Using professional formatting for the Excel output
            df.to_excel(self.file_name, index=False, engine='openpyxl')
            
            logging.info("✅ Synthesis Complete. Deployment Successful.")
        except Exception as e:
            logging.error(f"❌ Critical failure during synthesis: {e}")

if __name__ == "__main__":
    # Execute the engine
    engine = DataSynthesisEngine()
    engine.export()
    
    print("-" * 40)
    print(f"DEBUG: File '{engine.file_name}' is now available in the local directory.")
