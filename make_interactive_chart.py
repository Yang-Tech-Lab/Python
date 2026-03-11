"""
InsightEngine Pro: High-Fidelity BI Orchestration Suite
-------------------------------------------------------
An advanced data visualization engine that transforms transactional 
datasets into multi-dimensional, web-based intelligence platforms.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Full-Stack Data Engineering
Date: March 2026
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging
import sys
from pathlib import Path
from typing import Final, Optional

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class IntelligenceOrchestrator:
    def __init__(self, source_name: str = 'fiverr_report_finished.xlsx'):
        self.source_path: Final[Path] = Path(source_name)
        self.output_path: Final[Path] = Path('Vault/Executive_Dashboard_2026.html')
        self.theme: Final[str] = 'plotly_dark'
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Ensures the local persistence layer is provisioned."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        logging.info("🛠️ Orchestration environment synchronized.")

    def ingest_market_data(self) -> pd.DataFrame:
        """Loads and validates categorical transaction data."""
        logging.info(f"Ingesting raw data payload from: {self.source_path}")
        try:
            df = pd.read_excel(self.source_path)
            # Data Cleaning: Ensure numeric types for financial metrics
            df['销售总额'] = pd.to_numeric(df['销售总额'], errors='coerce').fillna(0)
            return df
        except Exception as e:
            logging.error(f"❌ Critical Ingestion Failure: {e}")
            sys.exit(1)

    def synthesize_visual_intelligence(self, df: pd.DataFrame) -> go.Figure:
        """Orchestrates the rendering of a multi-dimensional bar-treemap hybrid."""
        logging.info("Synthesizing interactive visual assets...")

        # 2. Advanced Multi-dimensional Visualization
        # Using a Treemap to show 'Market Share' alongside the Bar Chart
        fig = px.treemap(
            df,
            path=[px.Constant("Total Portfolio"), '产品名称'],
            values='销售总额',
            color='销售总额',
            color_continuous_scale='Viridis',
            title='Executive Market Share & Revenue Analysis',
            hover_data=['销售总额'],
            template=self.theme
        )

        # 3. Fine-tuning UX & Brand Identity
        fig.update_layout(
            title_font_size=28,
            title_x=0.5,
            font=dict(family="Inter, sans-serif", size=14),
            paper_bgcolor="#111111", # Ultra-dark tech aesthetic
            plot_bgcolor="#111111",
            margin=dict(t=100, b=50, l=50, r=50)
        )
        
        # Adding 'Strategic Annotations'
        fig.add_annotation(
            text="Yang-Tech-Lab Intelligence Engine | 2026 Edition",
            xref="paper", yref="paper",
            x=1, y=-0.1, showarrow=False,
            font=dict(size=10, color="gray")
        )

        return fig

    def deploy_dashboard(self):
        """Finalizes and persists the interactive intelligence asset."""
        data = self.ingest_market_data()
        figure = self.synthesize_visual_intelligence(data)
        
        logging.info(f"Persisting dynamic asset to: {self.output_path}")
        figure.write_html(
            str(self.output_path),
            include_plotlyjs='cdn', # Keeps file size small
            full_html=True
        )
        logging.info("🏆 Mission Accomplished. Intelligence Platform is live.")

if __name__ == "__main__":
    print("\n" + "="*55)
    print("      YANG-TECH-LAB: INSIGHT ENGINE ONLINE")
    print("="*55 + "\n")
    
    orchestrator = IntelligenceOrchestrator()
    orchestrator.deploy_dashboard()
