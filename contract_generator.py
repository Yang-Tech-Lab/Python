"""
LegalDoc Engine Pro: Automated Service Agreement Generator
----------------------------------------------------------
A high-performance document automation system designed to generate 
legally-structured Service Agreements for international clients.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Process Automation / LegalTech
"""

import os
import logging
from datetime import datetime
from typing import List, Dict
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 1. Initialize Professional Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class ContractEngine:
    def __init__(self, output_dir: str = "Generated_Contracts"):
        self.output_dir = output_dir
        self.provider_name = "Yang Jiacheng (Yang-Lab)"
        self._ensure_output_path()

    def _ensure_output_path(self):
        """Creates the target directory if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logging.info(f"Initialized output directory: {self.output_dir}")

    def generate(self, client_data: Dict[str, str]):
        """Generates a professional Service Agreement for a specific client."""
        client_name = client_data.get("name")
        service_scope = client_data.get("service")
        fee = client_data.get("price")

        doc = Document()

        # --- Section A: Document Header ---
        header = doc.add_heading('MASTER SERVICE AGREEMENT', 0)
        header.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # --- Section B: Metadata & Parties ---
        doc.add_paragraph(f"Execution Date: {datetime.now().strftime('%B %d, %Y')}")
        doc.add_paragraph(f"Client: {client_name}")
        doc.add_paragraph(f"Service Provider: {self.provider_name}")
        doc.add_paragraph("-" * 50)

        # --- Section C: Scope of Work (SOW) ---
        sow_title = doc.add_heading('1. Scope of Work', level=1)
        p1 = doc.add_paragraph("The Provider hereby agrees to perform the following professional services: ")
        run_service = p1.add_run(f"[{service_scope}]")
        run_service.bold = True
        run_service.font.color.rgb = RGBColor(44, 62, 80) # Dark Blue-Grey

        # --- Section D: Financial Terms ---
        fee_title = doc.add_heading('2. Consideration and Payment', level=1)
        p2 = doc.add_paragraph("In consideration for the services provided, the total project fee is fixed at: ")
        run_fee = p2.add_run(f"${fee} USD")
        run_fee.bold = True
        run_fee.font.size = Pt(12)
        run_fee.font.color.rgb = RGBColor(39, 174, 96) # Professional Emerald Green

        doc.add_paragraph("-" * 50)

        # --- Section E: Execution Block ---
        doc.add_paragraph("\n[SIGNATURE PAGE FOLLOWS]")
        doc.add_paragraph("\nBy: __________________________")
        doc.add_paragraph(f"Authorized Representative: {self.provider_name}")

        # Save the finalized document
        file_path = os.path.join(self.output_dir, f"Agreement_{client_name.replace(' ', '_')}.docx")
        doc.save(file_path)
        logging.info(f"Successfully compiled contract for: {client_name}")

    def batch_process(self, clients_list: List[Dict[str, str]]):
        """Processes multiple contracts in sequence."""
        logging.info(f"Starting batch production for {len(clients_list)} entities...")
        for client in clients_list:
            try:
                self.generate(client)
            except Exception as e:
                logging.error(f"Failed to process {client.get('name')}: {e}")
        logging.info("Batch operation completed successfully.")

if __name__ == "__main__":
    # Mock Enterprise Client Data
    # Including tech leaders to reflect your full-stack & hardware interests
    client_registry = [
        {"name": "Google Inc.", "price": "10,000", "service": "Automated Web Intelligence Pipeline"},
        {"name": "Tesla Motors", "price": "25,000", "service": "Embedded System & PCB Architecture"},
        {"name": "SpaceX", "price": "50,000", "service": "Full-Stack Aerospace Automation Suite"}
    ]

    # Execute the Engine
    engine = ContractEngine()
    engine.batch_process(client_registry)
