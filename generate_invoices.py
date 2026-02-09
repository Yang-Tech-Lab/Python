"""
FinDoc Architect: Professional Invoice Synthesis Engine
-------------------------------------------------------
A high-performance utility designed to generate legally-structured 
PDF invoices for enterprise-level service verification and testing.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Process Automation / Fintech
Date: February 2026
"""

import os
import random
import logging
from datetime import datetime
from typing import List, Final
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER

# 1. Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class InvoiceGenerator:
    def __init__(self, output_dir: str = "Financial_Vault"):
        self.output_dir: Final[str] = output_dir
        self.provider: Final[str] = "Yang Jiacheng (Full-Stack Engineer)"
        self._initialize_vault()

    def _initialize_vault(self):
        """Ensures the secure persistence layer (directory) is initialized."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logging.info(f"Financial Vault initialized at: {self.output_dir}")

    def generate_synthetic_invoice(self, client: str, index: int):
        """Generates a structured PDF invoice with randomized fiscal data."""
        # Strategic data generation
        amount = random.randint(1500, 12000)
        invoice_id = f"INV-{datetime.now().year}-{500 + index}"
        file_path = os.path.join(self.output_dir, f"Invoice_{client.replace(' ', '_')}.pdf")
        
        logging.info(f"Compiling fiscal record for: {client} | Target: {file_path}")

        try:
            # Document Canvas Initialization
            c = canvas.Canvas(file_path, pagesize=LETTER)
            
            # --- Visual Identity Section ---
            c.setFont("Helvetica-Bold", 24)
            c.setStrokeColorRGB(0.2, 0.2, 0.2)
            c.drawString(50, 750, "TAX INVOICE")
            
            # --- Entity Details ---
            c.setFont("Helvetica", 11)
            c.drawString(50, 720, f"Issued by: {self.provider}")
            c.drawString(50, 705, f"Recipient: {client}")
            c.drawString(50, 690, f"Date of Issue: {datetime.now().strftime('%B %d, %Y')}")
            
            # Horizontal Separator
            c.line(50, 675, 550, 675)
            
            # --- Service Description & Financials ---
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, 650, "Description of Services:")
            
            c.setFont("Helvetica", 11)
            c.drawString(70, 630, "• Full-Stack Software & Hardware Integration (IoT)")
            c.drawString(70, 615, "• Automated Workflow Development (Python/Selenium)")
            
            # Critical Data Points
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, 570, f"Invoice Reference: {invoice_id}")
            
            # Highlighted Remuneration
            c.setFillColorRGB(0.15, 0.68, 0.37) # Professional Emerald Green
            c.drawString(50, 550, f"Total Amount Due: ${amount:,.2f} USD")
            
            # --- Footer & Signature ---
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Helvetica-Oblique", 10)
            c.drawString(50, 100, "Note: This is a synthetically generated document for system verification.")
            
            c.save()
            logging.info(f"Successfully persisted invoice: {invoice_id}")
            
        except Exception as e:
            logging.error(f"Critical failure during document compilation for {client}: {e}")

    def process_client_registry(self, clients: List[str]):
        """Executes a batch generation sequence for a list of corporate entities."""
        logging.info(f"Initiating batch sequence for {len(clients)} entities...")
        for i, client in enumerate(clients):
            self.generate_synthetic_invoice(client, i)
        logging.info("Batch generation sequence finalized.")

if __name__ == "__main__":
    # Enterprise-level Mock Data (Reflecting your interest in tech giants)
    #
    corporate_partners = ["SpaceX", "Tesla Motors", "NVIDIA Corp", "Neuralink", "Apple Inc"]
    
    print("--- FinDoc Architect Engine Online ---")
    engine = InvoiceGenerator()
    engine.process_client_registry(corporate_partners)
    print("--- Session Terminated ---")
