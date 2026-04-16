"""
InsightOrchestrator Pro: v5.6 Global Enterprise Edition
-------------------------------------------------------
An industrial-grade BI engine designed for hierarchical market analysis, 
featuring deterministic data orchestration and interactive KPI telemetry.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Full-Stack Systems / Data Engineering
Date: April 15, 2026
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Final, Optional, List

# 1. Industrial Infrastructure & Telemetry Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("Vault/Logs/intelligence_audit.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class InsightOrchestrator:
    def __init__(self, source_node: str = 'fiverr_market_data.xlsx'):
        self.source_path: Final[Path] = Path(source_node)
        self.vault_path: Final[Path] = Path('Vault/Dashboards')
        self.theme: Final[str] = 'plotly_dark'
        self.brand_emerald: Final[str] = '#27AE60' # Success Metrics
        self.brand_navy: Final[str] = '#1B2631'    # Industrial Deep Navy
        
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure local storage and audit layers."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        Path("Vault/Logs").mkdir(parents=True, exist_ok=True)
        logging.info("🛠️ Orchestration vault synchronized. Environment: Production.")

    def _ingest_and_validate_telemetry(self) -> pd.DataFrame:
        """Loads raw telemetry and applies deterministic sanitization protocols."""
        logging.info(f"Ingesting market telemetry from: {self.source_path.name}")
        try:
            # Note: Expecting English headers: 'Product_Name', 'Total_Revenue'
            df = pd.read_excel(self.source_path)
            
            # Ensure numeric integrity for financial metrics
            # Logic: Convert to numeric, coerce errors to NaN, then fill with 0
            df['Total_Revenue'] = pd.to_numeric(df['Total_Revenue'], errors='coerce').fillna(0)
            
            # Feature Engineering: Calculate Relative Contribution
            # Formula: $$Contribution\_Pct = \frac{Value_{node}}{\sum Value_{total}} \times 100$$
            total_revenue = df['Total_Revenue'].sum()
            if total_revenue == 0:
                raise ValueError("Revenue node is null. Data ingestion aborted.")
                
            df['Contribution_Pct'] = (df['Total_Revenue'] / total_revenue * 100).round(2)
            
            return df
        except Exception as e:
            logging.error(f"❌ Ingestion Breach: {e}")
            raise

    def synthesize_platform_asset(self):
        """Orchestrates the synthesis of an interactive Sunburst Intelligence Platform."""
        df = self._ingest_and_validate_telemetry()
        logging.info("Synthesizing multi-dimensional visual intelligence...")

        # 2. Hierarchical Sunburst Orchestration
        # Sunburst is superior for nested categorical data in 2026-spec BI
        fig = px.sunburst(
            df,
            path=['Product_Name'], 
            values='Total_Revenue',
            color='Contribution_Pct',
            color_continuous_scale='Greens',
            title=f"Strategic Revenue Distribution | FY {datetime.now().year}",
            template=self.theme,
            hover_data={'Contribution_Pct': ':.2f}%'}
        )

        # 3. High-Fidelity UI/UX Refinement
        fig.update_layout(
            title_font=dict(size=26, family="Arial Black", color="white"),
            title_x=0.5,
            paper_bgcolor="#0A0A0A", # Cyber-Slate background
            plot_bgcolor="#0A0A0A",
            font=dict(family="Segoe UI", size=14),
            margin=dict(t=80, b=40, l=40, r=40)
        )

        # Professional Data Traces for Interactive Handshakes
        fig.update_traces(
            marker=dict(line=dict(color='#000000', width=1)),
            hovertemplate='<b>%{label}</b><br>Revenue: $%{value:,.2f}<br>Contribution: %{customdata[0]:.2f}%'
        )

        # 4. Strategic Persistence Layer
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        export_file = self.vault_path / f"Executive_Dashboard_{timestamp}.html"
        
        logging.info(f"Persisting dynamic asset to: {export_file.name}")
        fig.write_html(
            str(export_file),
            include_plotlyjs='cdn',
            full_html=True,
            auto_open=False
        )
        
        logging.info(f"🏆 Intelligence Node Online: {export_file.resolve()}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("      YANG-TECH-LAB: INSIGHT ORCHESTRATOR v5.6")
    print("="*60 + "\n")
    
    try:
        # Standard Operating Procedure (SOP) Initialization
        orchestrator = InsightOrchestrator(source_node='fiverr_market_data.xlsx')
        orchestrator.synthesize_platform_asset()
    except Exception as fatal_e:
        logging.critical(f"System Crash during orchestration: {fatal_e}")
    
    print("\n--- Synthesis Cycle Complete: Intelligence Asset Live ---")
