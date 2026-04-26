"""
FiscalIntelligence Orchestrator: Professional PDF Ingestion Engine
------------------------------------------------------------------
An industrial-grade utility designed to orchestrate the ingestion, 
regex-based extraction, and persistence of fiscal metrics from PDF assets.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Financial Automation
Date: April 21, 2026
"""

import re
import logging
import pandas as pd
import pdfplumber
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Final, Any

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("fiscal_ingestion_audit.log"),
        logging.StreamHandler()
    ]
)

class FiscalOrchestrator:
    def __init__(self, vault_dir: str = "Vault/Invoices"):
        self.vault_path: Final[Path] = Path(vault_dir)
        self.output_path: Final[Path] = Path("Vault/Exports/Strategic_Fiscal_Summary.xlsx")
        self.registry: List[Dict[str, Any]] = []
        
        # Professional Metadata
        self.provider_id: Final[str] = "Yang-Tech-Lab Execution Engine"
        self._bootstrap_vault()

    def _bootstrap_vault(self):
        """Provisions the secure local persistence layers."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"🛠️ Orchestration environment synchronized at: {self.vault_path.resolve()}")

    def _extract_deterministic_metrics(self, text: str) -> Dict[str, Optional[str]]:
        """
        Executes heuristic pattern matching using Regular Expressions (Regex).
        This ensures higher resilience against formatting variations.
        """
        # Logic: Pattern matching for common invoice schemas
        patterns = {
            "invoice_id": r"Invoice\s*Number:\s*(\w+)",
            "total_amount": r"Total\s*Amount:\s*\$?([\d,]+\.\d{2})",
            "date": r"Date:\s*([\w\s,]+)"
        }
        
        extracted = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            extracted[key] = match.group(1).replace(",", "") if match else None
            
        return extracted

    def execute_ingestion_pipeline(self):
        """Orchestrates the full lifecycle of PDF data acquisition."""
        logging.info("🚀 Initiating Deterministic Ingestion Sequence...")
        
        pdf_assets = list(self.vault_path.glob("*.pdf"))
        if not pdf_assets:
            logging.warning("⚠️ No PDF assets identified in the vault. System standing by.")
            return

        for pdf_asset in pdf_assets:
            try:
                with pdfplumber.open(pdf_asset) as pdf:
                    # Ingesting Primary Payload (First Page)
                    content = pdf.pages[0].extract_text()
                    
                    if not content:
                        logging.warning(f"Metadata Breach: Page content unreadable in {pdf_asset.name}")
                        continue

                    metrics = self._extract_deterministic_metrics(content)
                    
                    # Data Transformation & Integrity Check
                    amount_val = float(metrics.get("total_amount") or 0.0)
                    
                    self.registry.append({
                        "Sync_Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Source_Asset": pdf_asset.name,
                        "Invoice_Identifier": metrics.get("invoice_id") or "UNKNOWN",
                        "Valuation_USD": amount_val,
                        "Document_Status": "VERIFIED" if amount_val > 0 else "FLAGGED"
                    })
                    logging.info(f"   ✅ Node Synchronized: {pdf_asset.name} | Metric: ${amount_val:,.2f}")

            except Exception as e:
                logging.error(f"❌ Ingestion Fault in {pdf_asset.name}: {e}")

    def persist_to_vault(self):
        """Persists the acquired intelligence into a structured Excel binary."""
        if not self.registry:
            return

        df = pd.DataFrame(self.registry)
        
        # Strategic Intelligence Calculation
        # Formula: $$Total\_Exposure = \sum_{i=1}^{n} Invoice\_Amount_i$$
        total_aggregate = df["Valuation_USD"].sum()
        logging.info(f"💎 Cumulative Fiscal Ingestion: ${total_aggregate:,.2f}")

        try:
            # Professional Formatting Layer (XlsxWriter)
            with pd.ExcelWriter(self.output_path, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Fiscal_Intelligence')
                
                workbook = writer.book
                worksheet = writer.sheets['Fiscal_Intelligence']
                
                # Apply high-end aesthetic styles
                header_fmt = workbook.add_format({'bold': True, 'bg_color': '#2C3E50', 'font_color': 'white', 'border': 1})
                currency_fmt = workbook.add_format({'num_format': '$#,##0.00'})
                
                for col_num, value in enumerate(df.columns.values):
                    worksheet.write(0, col_num, value, header_fmt)
                    worksheet.set_column(col_num, col_num, 18)
                
                worksheet.set_column('D:D', 18, currency_fmt) # Column D: Valuation_USD

            logging.info(f"🏆 Strategic report deployed to secure vault: {self.output_path}")
        except Exception as e:
            logging.error(f"Persistence Layer Failure: {e}")

if __name__ == "__main__":
    print("\n" + "="*55)
    print("      YANG-TECH-LAB: FISCAL INTELLIGENCE CORE")
    print("="*55 + "\n")
    
    orchestrator = FiscalOrchestrator(vault_dir="Invoices")
    orchestrator.execute_ingestion_pipeline()
    orchestrator.persist_to_vault()
