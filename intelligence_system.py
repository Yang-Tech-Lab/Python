"""
FiscalArchitect Pro: v5.1 Enterprise Orchestration Suite
---------------------------------------------------------
A high-fidelity document synthesis engine designed for automated, 
audit-ready fiscal reporting and technical service verification.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Process Automation / Fintech
Date: April 12, 2026
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
        logging.FileHandler("Vault/Logs/fiscal_orchestration.log"),
        logging.StreamHandler()
    ]
)

@dataclass(frozen=True)
class ServiceNode:
    """Standardized data schema for high-fidelity service items."""
    description: str
    quantity: float
    unit_rate: float
    
    @property
    def subtotal(self) -> float:
        return round(self.quantity * self.unit_rate, 2)

class FiscalArchitect:
    def __init__(self, vault_dir: str = "Vault/Invoices"):
        self.vault_path: Final[Path] = Path(vault_dir)
        self.provider_id: Final[str] = "Yang Jiacheng (Yang-Tech-Lab)"
        self.tax_rate: Final[float] = 0.08  # Standardized 8% VAT for 2026
        self._bootstrap_vault()

    def _bootstrap_vault(self):
        """Provisions the secure persistence layer."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        Path("Vault/Logs").mkdir(parents=True, exist_ok=True)
        logging.info(f"🚀 Fiscal Intelligence Vault secured at: {self.vault_path.resolve()}")

    def _get_industrial_styles(self):
        """Orchestrates 2026-spec typography and branding aesthetics."""
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='EnterpriseHeader',
            fontSize=28,
            textColor=colors.HexColor("#1B2631"),
            fontName='Helvetica-Bold',
            spaceAfter=15
        ))
        styles.add(ParagraphStyle(
            name='FinancialHighlight',
            fontSize=14,
            textColor=colors.HexColor("#27AE60"),
            fontName='Helvetica-Bold'
        ))
        return styles

    def synthesize_fiscal_asset(self, client: str, nodes: List[ServiceNode]):
        """Orchestrates the synthesis of a structured, audit-ready PDF invoice."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        target_file = self.vault_path / f"INV_{client.replace(' ', '_')}_{timestamp}.pdf"
        
        # Document Template Setup
        doc = SimpleDocTemplate(
            str(target_file), 
            pagesize=A4, 
            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
        )
        
        styles = self._get_industrial_styles()
        story = [] # Flowable elements buffer

        # --- Phase 1: Header & Identity ---
        story.append(Paragraph("TAX INVOICE", styles['EnterpriseHeader']))
        
        meta_table_data = [
            [Paragraph(f"<b>PROVIDER:</b><br/>{self.provider_id}<br/>Guangzhou, PRC", styles['Normal']),
             Paragraph(f"<b>RECIPIENT:</b><br/>{client}<br/>Global Strategic Partner", styles['Normal'])]
        ]
        meta_table = Table(meta_table_data, colWidths=[3.5*inch, 3.5*inch])
        meta_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
        story.append(meta_table)
        story.append(Spacer(1, 0.4 * inch))

        # --- Phase 2: Itemized Service Ingestion ---
        # Calculation Formula:
        # $$Total_{Due} = \sum_{i=1}^{n} (Quantity_i \times Rate_i) \times (1 + Tax\_Rate)$$
        
        table_payload = [['DESCRIPTION', 'QTY', 'UNIT RATE', 'SUBTOTAL (USD)']]
        gross_sum = 0.0
        
        for node in nodes:
            table_payload.append([
                node.description,
                f"{node.quantity:.1f}",
                f"${node.unit_rate:,.2f}",
                f"${node.subtotal:,.2f}"
            ])
            gross_sum += node.subtotal

        # Tax Calculation logic
        tax_amount = gross_sum * self.tax_rate
        total_payable = gross_sum + tax_amount

        # Table Styling Orchestration
        t = Table(table_payload, colWidths=[3.8*inch, 0.8*inch, 1.2*inch, 1.2*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2C3E50")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white])
        ]))
        story.append(t)
        story.append(Spacer(1, 0.3 * inch))

        # --- Phase 3: Financial Summary ---
        summary_data = [
            ['', 'GROSS SUBTOTAL:', f"${gross_sum:,.2f}"],
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

        # --- Phase 4: Legal & System Footer ---
        story.append(Spacer(1, 1.5 * inch))
        footer_style = ParagraphStyle(name='Footer', fontSize=7, textColor=colors.grey, alignment=1)
        story.append(Paragraph("System-generated financial asset. Non-transferable digital audit trail active.", footer_style))
        story.append(Paragraph(f"Yang-Tech-Lab Core Infrastructure | {datetime.now().isoformat()}", footer_style))

        # Build Final Asset
        try:
            doc.build(story)
            logging.info(f"✅ Strategic asset persisted: {target_file.name}")
        except Exception as e:
            logging.error(f"❌ Synthesis Failure: {e}")

if __name__ == "__main__":
    # Operational Deployment: 2026-04-12
    print("\n" + "="*55)
    print("      YANG-TECH-LAB: FISCAL ARCHITECT PRO v5.1")
    print("="*55 + "\n")
    
    architect = FiscalArchitect()
    
    # Mock Strategic Payload (Soft-Hard Integration Focus)
    service_nodes = [
        ServiceNode("Automated PCB DFM Validation Script (KiCad 9.0 API)", 1, 2800.00),
        ServiceNode("ESP32 IoT Sensor Mesh Architecture (Firmware)", 45, 120.00),
        ServiceNode("Selenium-driven Market Intelligence Engine", 1, 1500.00)
    ]
    
    architect.synthesize_fiscal_asset(client="SpaceX (Starlink Ground Node)", nodes=service_nodes)
    print("\n--- Synthesis Cycle Complete: Assets Synchronized ---")
