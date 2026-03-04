"""
JurisOrchestrator Pro: Advanced Legal Synthesis Engine
------------------------------------------------------
A high-fidelity document automation suite designed to synthesize 
Master Service Agreements (MSA) with enterprise-grade typography, 
standardized legal clauses, and automated audit trails.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: LegalTech / Process Automation
Date: March 2026
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Final, TypedDict

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class ClientProfile(TypedDict):
    name: str
    price: str
    service: str
    jurisdiction: str

class JurisOrchestrator:
    def __init__(self, output_dir: str = "Vault/Contracts"):
        self.output_path = Path(output_dir)
        self.provider_id: Final[str] = "Yang Jiacheng (Yang-Tech-Lab)"
        self.brand_color: Final[RGBColor] = RGBColor(28, 40, 51)  # Deep Charcoal Navy
        self.accent_color: Final[RGBColor] = RGBColor(39, 174, 96) # Emerald Success Green
        self._provision_storage()

    def _provision_storage(self):
        """Ensures the persistence layer is initialized."""
        if not self.output_path.exists():
            self.output_path.mkdir(parents=True)
            logging.info(f"Initialized secure storage at: {self.output_path}")

    def _apply_typography(self, paragraph, size=11, bold=False, color=None):
        """Standardizes font styling across the document lifecycle."""
        run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
        run.font.name = 'Cambria'  # Professional Serif Typography
        run.font.size = Pt(size)
        run.font.bold = bold
        if color:
            run.font.color.rgb = color

    def synthesize_msa(self, client: ClientProfile):
        """Orchestrates the synthesis of a Master Service Agreement."""
        logging.info(f"Synthesizing MSA for entity: {client['name']}")
        doc = Document()

        # --- Phase 1: Header & Titling ---
        header = doc.add_heading('MASTER SERVICE AGREEMENT', 0)
        header.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # --- Phase 2: Engagement Metadata ---
        meta_p = doc.add_paragraph()
        meta_p.add_run(f"Reference ID: MSA-{datetime.now().strftime('%Y%m%d')}-{client['name'][:3].upper()}\n")
        meta_p.add_run(f"Effective Date: {datetime.now().strftime('%B %d, %Y')}\n")
        meta_p.add_run(f"Jurisdiction: {client['jurisdiction']}")
        self._apply_typography(meta_p, size=10)

        # --- Phase 3: Scope of Professional Services ---
        doc.add_heading('1. SCOPE OF ENGAGEMENT', level=1)
        sow_p = doc.add_paragraph(
            f"The Provider agrees to deploy specialized technical services including, "
            f"but not limited to: "
        )
        sow_run = sow_p.add_run(client['service'])
        sow_run.bold = True
        sow_run.font.color.rgb = self.brand_color

        # --- Phase 4: Financial Consideration ---
        doc.add_heading('2. FINANCIAL TERMS', level=1)
        fee_p = doc.add_paragraph("Total consideration for the defined sprint/project is fixed at: ")
        fee_run = fee_p.add_run(f"${client['price']} USD")
        fee_run.bold = True
        fee_run.font.size = Pt(12)
        fee_run.font.color.rgb = self.accent_color

        # --- Phase 5: IP & Confidentiality (Standard Legal Boilerplate) ---
        doc.add_heading('3. INTELLECTUAL PROPERTY', level=1)
        doc.add_paragraph(
            "All technical deliverables, including source code, PCB schematics, and "
            "automated scripts, shall be transferred to the Client upon full settlement of fees."
        )

        # --- Phase 6: Execution Block ---
        doc.add_paragraph("\n" + "="*40)
        doc.add_paragraph("IN WITNESS WHEREOF, the parties have executed this Agreement.")
        
        sign_table = doc.add_table(rows=2, cols=2)
        sign_table.cell(0, 0).text = "CLIENT SIGNATURE"
        sign_table.cell(0, 1).text = "PROVIDER SIGNATURE"
        sign_table.cell(1, 0).text = f"\n\n________________\n{client['name']}"
        sign_table.cell(1, 1).text = f"\n\n________________\n{self.provider_id}"

        # Persistence
        safe_name = client['name'].replace(" ", "_")
        target_file = self.output_path / f"MSA_Final_{safe_name}.docx"
        doc.save(str(target_file))
        logging.info(f"✅ MSA successfully persisted to: {target_file.name}")

    def execute_batch(self, registry: List[ClientProfile]):
        """Executes high-volume document synthesis."""
        logging.info(f"🚀 Initiating batch synthesis for {len(registry)} strategic nodes.")
        for entity in registry:
            try:
                self.synthesize_msa(entity)
            except Exception as e:
                logging.error(f"Critical failure during synthesis for {entity['name']}: {e}")

if __name__ == "__main__":
    # Enterprise-grade Client Registry
    client_nodes: List[ClientProfile] = [
        {
            "name": "Neuralink Corp", 
            "price": "35,000", 
            "service": "Bio-Signal Automation Pipeline", 
            "jurisdiction": "California, USA"
        },
        {
            "name": "NVIDIA", 
            "price": "12,000", 
            "service": "Automated Hardware Validation Suite", 
            "jurisdiction": "Delaware, USA"
        }
    ]

    # Initialize Engine
    print("--- JurisOrchestrator Core: System Online ---")
    engine = JurisOrchestrator()
    engine.execute_batch(client_nodes)
    print("--- Batch Operations Concluded ---")
