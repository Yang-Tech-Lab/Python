"""
FiscalOrchestrator Pro: Industrial-Grade Fiscal Ingestion Engine
----------------------------------------------------------------
A high-performance orchestration suite designed to ingest, process, 
and synthesize strategic financial telemetry for enterprise-level reporting.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Automation
Date: April 26,2026
"""

import logging
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Final, List, Dict, Optional

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("fiscal_audit.log"),
        logging.StreamHandler()
    ]
)

class FiscalOrchestrator:
    def __init__(self, input_file: str = "raw_sales_data.xlsx"):
        self.input_path: Final[Path] = Path(input_file)
        self.vault_path: Final[Path] = Path("Vault/Exports")
        self.registry: Optional[pd.DataFrame] = None
        
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure local persistence layers."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        if not self.input_path.exists():
            logging.error(f"❌ Handshake Failure: Input asset '{self.input_path}' not identified.")
        else:
            logging.info("🛠️ Fiscal environment synchronized. Ready for ingestion.")

    def execute_ingestion_pipeline(self):
        """Orchestrates the data acquisition and transformation sequence."""
        if not self.input_path.exists(): return

        logging.info(f"🚀 Initiating Fiscal Ingestion: {self.input_path.name}")
        
        try:
            # 1. Data Ingestion
            df = pd.read_excel(self.input_path)
            
            # 2. Transformation Layer (Feature Engineering)
            # Logic: Strategic Revenue = Unit Price * Quantity
            df['Gross_Revenue'] = df['Unit_Price'] * df['Quantity']
            
            # Additional KPI: Estimating Net Margin (Assume 15% Platform Overhead)
            df['Net_Margin_Est'] = df['Gross_Revenue'] * 0.85
            
            # 3. Metadata Injection
            df['Sync_Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            self.registry = df
            
            total_valuation = df['Gross_Revenue'].sum()
            logging.info(f"✅ Ingestion Complete. Cumulative Valuation: ${total_valuation:,.2f}")

        except Exception as e:
            logging.error(f"❌ Pipeline Breach: {e}")

    def persist_strategic_report(self, filename: str = "Strategic_Fiscal_Analysis.xlsx"):
        """Persists the processed intelligence to a high-fidelity Excel binary."""
        if self.registry is None:
            logging.warning("No data available in the registry for persistence.")
            return

        target_file = self.vault_path / filename
        logging.info(f"💾 Deploying high-fidelity asset to: {target_file}")

        try:
            # Using XlsxWriter for "Premium" report aesthetics
            with pd.ExcelWriter(target_file, engine='xlsxwriter') as writer:
                self.registry.to_excel(writer, index=False, sheet_name='Intelligence_Report')
                
                workbook = writer.book
                worksheet = writer.sheets['Intelligence_Report']
                
                # --- Industrial Styling Protocol ---
                header_fmt = workbook.add_format({
                    'bold': True, 'font_color': 'white', 'bg_color': '#1B2631', 'border': 1
                })
                currency_fmt = workbook.add_format({'num_format': '$#,##0.00'})
                
                # Apply Header Format & Column Scaling
                for col_num, value in enumerate(self.registry.columns.values):
                    worksheet.write(0, col_num, value, header_fmt)
                    worksheet.set_column(col_num, col_num, 18)
                
                # Highlight Financial Columns
                worksheet.set_column('C:E', 18, currency_fmt) 
            
            logging.info(f"🏆 Mission Accomplished. Strategic report deployed.")
            
        except Exception as e:
            logging.error(f"❌ Persistence Layer Failure: {e}")

if __name__ == "__main__":
    print("\n" + "="*55)
    print("      YANG-TECH-LAB: FISCAL ORCHESTRATOR PRO")
    print("="*55 + "\n")
    
    # Execution Lifecycle
    orchestrator = FiscalOrchestrator(input_file="fiverr_sales.xlsx")
    orchestrator.execute_ingestion_pipeline()
    orchestrator.persist_strategic_report()
