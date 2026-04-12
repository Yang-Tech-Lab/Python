"""
FiscalArchitect Pro: v5.0 Enterprise Orchestration Engine
---------------------------------------------------------
A high-fidelity document synthesis suite designed for automated, 
audit-ready fiscal reporting and technical service verification.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Process Automation / Fintech
Date: April 11, 2026
"""

import logging
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Final, Optional, Any

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# 1. Industrial Infrastructure Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("Vault/Logs/fiscal_synthesis.log"),
        logging.StreamHandler()
    ]
)

@dataclass(frozen=True)
class ServiceNode:
    """Standardized data schema for high-fidelity service items."""
    description: str
    quantity: float
    unit_rate: float
    tax_exempt: bool = False

    @property
    def subtotal(self) -> float:
        return round(self.quantity * self.unit_rate, 2)

class FiscalArchitect:
    def __init__(self, vault_dir: str = "Vault/Invoices"):
        self.vault_path: Final[Path] = Path(vault_dir)
        self.provider_id: Final[str] = "Yang Jiacheng (Yang-Tech-Lab)"
        self.tax_rate: Final[float] = 0.08  # Standardized 8% VAT
        self._bootstrap_vault()

    def _bootstrap_vault(self):
        """Provisions the secure persistence layer."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        Path("Vault/Logs").mkdir(parents=True, exist_ok=True)
        logging.info(f"🛠️ Orchestration vault synchronized: {self.vault_path.resolve()}")

    def _get_industrial_styles(self):
        """Orchestrates 2026-spec typography and aesthetics."""
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='EnterpriseHeader',
            fontSize=28,
            textColor=colors.HexColor("#1B2631"),
            fontName='Helvetica-Bold',
            spaceAfter=12
        ))
        styles.add(ParagraphStyle(
            name='MetadataLabel',
            fontSize=9,
            textColor=colors.grey,
            fontName='Helvetica-Oblique'
        ))
        return styles

    def synthesize_fiscal_asset(self, client: str, nodes: List[ServiceNode]):
        """Orchestrates the synthesis of a structured, audit-ready PDF asset."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = self.vault_path / f"INV_{client.replace(' ', '_')}_{timestamp}.pdf"
        
        doc = SimpleDocTemplate(str(filename), pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
        styles = self._get_industrial_styles()
        story = []

        # --- Phase 1: Branding & Identification ---
        story.append(Paragraph("TAX INVOICE", styles['EnterpriseHeader']))
        
        # Metadata Grid: From/To Layout
        meta_data = [
            [Paragraph(f"<b>FROM:</b><br/>{self.provider_id}<br/>Guangzhou, PRC", styles['Normal']),
             Paragraph(f"<b>TO:</b><br/>{client}<br/>Strategic Partner Node", styles['Normal'])]
        ]
        meta_table = Table(meta_data, colWidths=[3.5*inch, 3.5*inch])
        meta_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
        story.append(meta_table)
        story.append(Spacer(1, 0.4 * inch))

        # --- Phase 2: Transaction Telemetry ---
        story.append(Paragraph(f"Synchronization Date: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
        story.append(Paragraph(f"Asset Reference: {timestamp}-GZ", styles['MetadataLabel']))
        story.append(Spacer(1, 0.2 * inch))

        # --- Phase 3: Financial Orchestration (Table) ---
        table_payload = [['DESCRIPTION', 'QTY', 'RATE (USD)', 'AMOUNT']]
        gross_total = 0.0
        
        for node in nodes:
            table_payload.append([
                node.description,
                f"{node.quantity:.1f}",
                f"${node.unit_rate:,.2f}",
                f"${node.subtotal:,.2f}"
            ])
            gross_total += node.subtotal

        # Financial Calculation Logic
        tax_amount = gross_total * self.tax_rate
        total_payable = gross_total + tax_amount

        # Table Aesthetics
        t = Table(table_payload, colWidths=[3.8*inch, 0.8*inch, 1.2*inch, 1.2*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1B2631")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white])
        ]))
        story.append(t)

        # --- Phase 4: Fiscal Summary ---
        story.append(Spacer(1, 0.3 * inch))
        summary_data = [
            ['', 'SUBTOTAL:', f"${gross_total:,.2f}"],
            ['', f'VAT ({self.tax_rate*100:.0f}%):', f"${tax_amount:,.2f}"],
            ['', 'TOTAL PAYABLE:', f"${total_payable:,.2f}"]
        ]
        summary_table = Table(summary_data, colWidths=[4*inch, 1.5*inch, 1.5*inch])
        summary_table.setStyle(TableStyle([
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (1, 2), (-1, 2), 'Helvetica-Bold'),
            ('TEXTCOLOR', (1, 2), (-1, 2), colors.HexColor("#27AE60")),
            ('FONTSIZE', (1, 2), (-1, 2), 12),
        ]))
        story.append(summary_table)

        # --- Phase 5: Legal & System Footer ---
        story.append(Spacer(1, 1.5 * inch))
        footer_style = ParagraphStyle(name='Footer', fontSize=7, textColor=colors.grey, alignment=1)
        story.append(Paragraph("System-generated financial asset. Non-transferable digital trail.", footer_style))
        story.append(Paragraph(f"Yang-Tech-Lab Infrastructure | {datetime.now().isoformat()}", footer_style))

        # Build Protocol
        try:
            doc.build(story)
            logging.info(f"🏆 Strategic asset persisted: {filename.name}")
        except Exception as e:
            logging.error(f"❌ Ingestion Breach: {e}")

if __name__ == "__main__":
    # Operational Deployment: April 10, 2026
    print("\n" + "="*60)
    print("       YANG-TECH-LAB: FISCAL ARCHITECT PRO v5.0")
    print("="*60 + "\n")
    
    orchestrator = FiscalArchitect()
    
    # Standard Operating Procedure (SOP) Items
    service_nodes = [
        ServiceNode("Industrial PCB Design - High-Speed DDR4 Routing", 1, 3500.00),
        ServiceNode("ESP32-S3 Mesh Network Firmware (Optimization)", 24, 120.00),
        ServiceNode("Automated Market Intelligence Pipeline (Python)", 1, 1800.00)
    ]
    
    orchestrator.synthesize_fiscal_asset(
        client="SpaceX (Starlink Ground Station)", 
        nodes=service_nodes
    )
    print("\n--- Synthesis Cycle Complete: Assets Synchronized ---")
