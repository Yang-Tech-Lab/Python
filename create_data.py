"""
SalesOrchestrator Pro: Enterprise Strategic Synthesis Engine
------------------------------------------------------------
An industrial-grade ETL utility designed to synthesize high-variance, 
non-linear e-commerce datasets for algorithmic stress-testing.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Quantitative Analytics
Date: May 3, 2026
"""

import pandas as pd
import numpy as np
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Final, Dict, List, Optional

# 1. Industrial Infrastructure & Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("Vault/Logs/synthesis_audit.log"),
        logging.StreamHandler()
    ]
)

class SalesOrchestrator:
    def __init__(self, market_scenario: str = "Bullish"):
        self.vault_path: Final[Path] = Path("Vault/Exports")
        self.tax_rate: Final[float] = 0.13  # Updated 2026 Fiscal Standard
        self.scenario: str = market_scenario
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure local storage for synthesized intelligence."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"🛠️ Orchestration environment synchronized. Scenario: {self.scenario}")

    def _apply_market_volatility(self, base_price: float) -> float:
        """Applies a Gaussian noise factor to simulate 2026 market fluctuations."""
        # Bullish: +2% bias, Bearish: -3% bias
        bias = 1.02 if self.scenario == "Bullish" else 0.97
        noise = np.random.normal(bias, 0.05) 
        return round(base_price * noise, 2)

    def _synthesize_high_fidelity_nodes(self, volume: int) -> pd.DataFrame:
        """
        Synthesizes transaction nodes using non-linear distributions.
        Leverages Pareto Distribution for realistic '80/20' quantity modeling.
        """
        logging.info(f"🚀 Initiating synthesis cycle for {volume} strategic nodes...")

        # 2026 High-End Asset Registry
        assets = {
            'MacBook Pro M5 (Ultra)': 3299.00,
            'iPhone 18 Pro Max': 1499.00,
            'Vision Pro Gen 2': 3899.00,
            'Yang-Lab IoT Gateway v4': 450.00,
            'Studio Display XDR': 1999.00
        }

        # Non-linear quantity generation (Pareto: most orders are small, few are bulk)
        quantities = (np.random.pareto(3, volume) + 1) * 2
        quantities = quantities.astype(int)

        data_nodes = []
        start_date = datetime.now() - timedelta(days=30)

        for i in range(volume):
            product = np.random.choice(list(assets.keys()))
            base_p = assets[product]
            market_p = self._apply_market_volatility(base_p)
            
            # Simulated Cost of Goods Sold (COGS) at 65% of base
            cogs = round(base_p * 0.65, 2)
            qty = quantities[i]
            
            timestamp = start_date + timedelta(hours=np.random.randint(0, 720))
            
            data_nodes.append({
                'Transaction_ID': f"TXN-26-{i:05}",
                'Timestamp': timestamp.strftime("%Y-%m-%d %H:%M"),
                'Asset_Identifier': product,
                'Unit_Valuation': market_p,
                'Quantity': qty,
                'Region': np.random.choice(['Guangdong', 'Silicon Valley', 'Singapore', 'London']),
                'COGS_Unit': cogs
            })

        df = pd.DataFrame(data_nodes)

        # --- Phase 2: Feature Engineering & Fiscal Orchestration ---
        # Formula: $$Revenue_{Gross} = P \times Q$$
        df['Gross_Revenue'] = df['Unit_Valuation'] * df['Quantity']
        
        # Formula: $$Margin_{Net} = (Revenue_{Gross} - (COGS \times Q)) \times (1 - Tax)$$
        df['Net_Profit'] = ((df['Gross_Revenue'] - (df['COGS_Unit'] * df['Quantity'])) * (1 - self.tax_rate)).round(2)
        
        return df.sort_values(by='Timestamp')

    def deploy_intelligence_asset(self, record_count: int = 50):
        """Persists the intelligence payload with professional conditional formatting."""
        df = self._synthesize_high_fidelity_nodes(record_count)
        export_file = self.vault_path / f"Global_Sales_Intelligence_{datetime.now().strftime('%m%d')}.xlsx"

        try:
            with pd.ExcelWriter(export_file, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Data_Pulse')
                
                workbook = writer.book
                worksheet = writer.sheets['Data_Pulse']

                # --- Industrial Aesthetics ---
                header_fmt = workbook.add_format({'bold': True, 'font_color': 'white', 'bg_color': '#0E1117', 'border': 1})
                currency_fmt = workbook.add_format({'num_format': '$#,##0.00'})
                profit_fmt = workbook.add_format({'font_color': '#27AE60', 'bold': True}) # Success Green

                # Apply Header Styling
                for col_num, value in enumerate(df.columns.values):
                    worksheet.write(0, col_num, value, header_fmt)
                    worksheet.set_column(col_num, col_num, 20)

                # Applying High-Fidelity Conditional Formatting to Net_Profit
                # Highlight top 10% of profitable transactions in Green
                worksheet.conditional_format('I2:I500', {
                    'type': 'data_bar',
                    'bar_color': '#3498DB'
                })

                worksheet.set_column('D:D', 15, currency_fmt)
                worksheet.set_column('G:I', 18, currency_fmt)

            logging.info(f"🏆 Strategic asset deployed to vault: {export_file.name}")
        except Exception as e:
            logging.error(f"❌ Persistence Layer Breach: {e}")

if __name__ == "__main__":
    print("\n" + "="*55)
    print("      YANG-TECH-LAB: SALES INTELLIGENCE CORE")
    print("="*55 + "\n")
    
    orchestrator = SalesOrchestrator(market_scenario="Bullish")
    orchestrator.deploy_intelligence_asset(record_count=40)
    
    print("\n--- Synthesis Cycle Terminated ---")

