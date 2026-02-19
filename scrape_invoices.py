"""
FinData-Extractor Pro: Automated PDF Fiscal Intelligence Engine
---------------------------------------------------------------
A high-performance utility designed to parse, validate, and persist 
structured financial data from PDF invoices using heuristic text extraction.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Automation
Date: February 2026
"""

import pdfplumber
import pandas as pd
import logging
from pathlib import Path
from typing import List, Dict, Optional

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class FinanceOrchestrator:
    def __init__(self, input_dir: str = "Invoices", output_file: str = "Fiscal_Summary_Report.xlsx"):
        self.input_path = Path(input_dir)
        self.output_file = output_file
        self.registry: List[Dict] = []
        
        # Ensure the persistence layer directory exists
        if not self.input_path.exists():
            logging.error(f"Directory {input_dir} not found. Please verify the asset path.")

    def extract_heuristic_data(self, text: str) -> Dict[str, str]:
        """Performs targeted text segmentation to identify key financial metrics."""
        results = {"invoice_num": "N/A", "amount": "0.0"}
        
        for line in text.split('\n'):
            # Segmenting Invoice Identifier
            if "Invoice Number:" in line:
                results["invoice_num"] = line.split(":")[-1].strip()
            
            # Segmenting Monetary Value
            if "Total Amount:" in line:
                # Sanitizing currency symbols and whitespace
                raw_amount = line.split(":")[-1].replace("$", "").strip()
                results["amount"] = raw_amount
                
        return results

    def run_acquisition_pipeline(self):
        """Orchestrates the full lifecycle of PDF ingestion and data parsing."""
        logging.info("🚀 Initiating Financial Intelligence Pipeline...")
        
        pdf_assets = list(self.input_path.glob("*.pdf"))
        logging.info(f"Detected {len(pdf_assets)} PDF assets for processing.")

        for pdf_file in pdf_assets:
            try:
                with pdfplumber.open(pdf_file) as pdf:
                    # Ingesting the primary page for metadata extraction
                    primary_page = pdf.pages[0]
                    content = primary_page.extract_text()
                    
                    if not content:
                        logging.warning(f"Metadata missing or unreadable in: {pdf_file.name}")
                        continue

                    metrics = self.extract_heuristic_data(content)
                    
                    self.registry.append({
                        "Source_File": pdf_file.name,
                        "Invoice_ID": metrics["invoice_num"],
                        "Total_USD": float(metrics["amount"])
                    })
                    logging.info(f"Successfully synchronized: {pdf_file.name} | Total: ${metrics['amount']}")

            except Exception as e:
                logging.error(f"Critical failure during ingestion of {pdf_file.name}: {e}")

    def export_intelligence_report(self):
        """Persists the extracted dataset into a structured Excel binary."""
        if not self.registry:
            logging.warning("No validated data available for persistence.")
            return

        df = pd.DataFrame(self.registry)
        
        # Generate fiscal insights (The 'Client Surprise' metric)
        total_aggregate = df["Total_USD"].sum()
        logging.info(f"💎 Cumulative Asset Valuation: ${total_aggregate:,.2f}")

        df.to_excel(self.output_file, index=False)
        logging.info(f"✅ Intelligence report persisted: [{self.output_file}]")

if __name__ == "__main__":
    # Deployment in Guangzhou Local Environment
    #
    engine = FinanceOrchestrator(input_dir="Invoices")
    engine.run_acquisition_pipeline()
    engine.export_intelligence_report()
