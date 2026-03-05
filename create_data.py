"""
SalesData Synthesis Engine Pro (Enterprise)
-------------------------------------------
An advanced ETL utility designed to synthesize high-variance e-commerce 
datasets for system stress-testing and financial modeling.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Intelligence
Date: March 2026
"""

import pandas as pd
import numpy as np
import logging
from pathlib import Path
from datetime import datetime
from typing import Final, Dict, List

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class SalesSynthesisOrchestrator:
    def __init__(self, export_name: str = "Corporate_Sales_Intelligence.xlsx"):
        self.export_path: Final[Path] = Path("Vault/Exports") / export_name
        self.tax_rate: Final[float] = 0.15  # Standardized 15% VAT/GST
        self._ensure_infrastructure()

    def _ensure_infrastructure(self):
        """Ensures the persistence layer directory exists."""
        self.export_path.parent.mkdir(parents=True, exist_ok=True)

    def _generate_synthetic_payload(self, records: int = 50) -> pd.DataFrame:
        """Synthesizes a high-variance dataset using numpy-driven distributions."""
        logging.info(f"Synthesizing {records} high-fidelity transaction nodes...")
        
        products = {
            'MacBook Pro M5': 2899.00, # 2026 Spec
            'iPhone 18 Pro': 1299.00,
            'iPad Pro Gen 8': 1099.00,
            'Apple Vision Pro 2': 3499.00,
            'AirPods Max 2': 549.00
        }

        # Randomized generation logic
        selected_prods = np.random.choice(list(products.keys()), records)
        base_prices = [products[p] for p in selected_prods]
        quantities = np.random.randint(1, 15, size=records)
        regions = np.random.choice(['NA', 'EMEA', 'APAC', 'LATAM'], records)

        df = pd.DataFrame({
            'Transaction_ID': [f"TXN-2026-{i:04}" for i in range(records)],
            'Product_Line': selected_prods,
            'Unit_Price': base_prices,
            'Quantity': quantities,
            'Region': regions,
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # 2. Advanced Feature Engineering
        # Formula: $$Revenue_{Gross} = P \times Q$$
        df['Gross_Revenue'] = df['Unit_Price'] * df['Quantity']
        
        # Formula: $$Tax_{Amount} = Revenue_{Gross} \times Tax_{Rate}$$
        df['Tax_Component'] = (df['Gross_Revenue'] * self.tax_rate).round(2)
        
        # Formula: $$Revenue_{Net} = Revenue_{Gross} + Tax_{Amount}$$
        df['Total_Payable'] = df['Gross_Revenue'] + df['Tax_Component']
        
        return df

    def deploy_analytics_report(self, volume: int = 100):
        """Persists the synthesized data into a professionally formatted Excel binary."""
        try:
            df = self._generate_synthetic_payload(records=volume)
            logging.info(f"Orchestrating professional export to: {self.export_path}")

            # Using XlsxWriter for premium formatting
            with pd.ExcelWriter(self.export_path, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sales_Intelligence')
                
                workbook = writer.book
                worksheet = writer.sheets['Sales_Intelligence']

                # --- High-End Styling ---
                header_fmt = workbook.add_format({
                    'bold': True, 'font_color': 'white', 'bg_color': '#1B2631', 'border': 1
                })
                currency_fmt = workbook.add_format({'num_format': '$#,##0.00'})

                # Formatting the headers and adjusting column width
                for col_num, value in enumerate(df.columns.values):
                    worksheet.write(0, col_num, value, header_fmt)
                    worksheet.set_column(col_num, col_num, 18)

                # Applying currency format to financial columns
                worksheet.set_column('C:C', 15, currency_fmt) # Unit Price
                worksheet.set_column('G:I', 18, currency_fmt) # Revenue Columns

            logging.info("✅ Deployment Successful. Strategic asset ready for client delivery.")
        except Exception as e:
            logging.error(f"❌ Critical Failure in Data Pipeline: {e}")

if __name__ == "__main__":
    print("--- Yang-Tech-Lab Data Intelligence Suite Online ---")
    orchestrator = SalesSynthesisOrchestrator()
    orchestrator.deploy_analytics_report(volume=25)
    print("-" * 55)
