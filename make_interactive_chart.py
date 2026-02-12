 """
Interactive Insight Engine: Executive Sales Dashboard
-----------------------------------------------------
A high-performance visualization suite that converts transactional data 
into a dynamic, web-based Business Intelligence (BI) dashboard.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Full-Stack Data Visualization
Date: February 2026
"""

import pandas as pd
import plotly.express as px
import logging
import sys
from typing import Final

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Configuration Constants
SOURCE_FILE: Final[str] = 'fiverr_report_finished.xlsx'
OUTPUT_DASHBOARD: Final[str] = 'interactive_business_intelligence.html'

class DashboardEngine:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.theme = 'plotly_dark'  # High-tech aesthetic for professional engineering reports

    def ingest_data(self) -> pd.DataFrame:
        """Loads and validates the transaction dataset."""
        logging.info(f"Ingesting data from: {self.data_path}")
        try:
            return pd.read_excel(self.data_path)
        except FileNotFoundError:
            logging.error(f"Critical Error: Source file '{self.data_path}' not found.")
            sys.exit(1)

    def compile_dashboard(self):
        """Orchestrates the visualization rendering and persistence sequence."""
        df = self. ingest_data()
        
        logging.info("Initializing Plotly rendering engine...")
        
        # 2. Interactive Bar Chart Architecture
        # Translating Chinese headers to standard English business metrics
        fig = px.bar(
            df, 
            x='产品名称', 
            y='销售总额',
            color='销售总额',
            color_continuous_scale=px.colors.sequential.Viridis,
            title='Executive Sales Performance Analytics',
            labels={'产品名称': 'Product Category', '销售总额': 'Revenue (USD)'},
            text_auto='.2s',
            template=self.theme
        )

        # 3. Fine-tuning Layout for Enterprise Standards
        fig.update_layout(
            title_font_size=24,
            title_x=0.5, # Center the title
            xaxis_tickangle=-45,
            font=dict(family="Courier New, monospace", size=14, color="white"),
            margin=dict(l=50, r=50, t=100, b=100),
            paper_bgcolor="#1e1e1e", # Deep charcoal for a premium feel
            plot_bgcolor="#1e1e1e"
        )

        # 4. Persistence Layer
        logging.info(f"Exporting dynamic assets to: {OUTPUT_DASHBOARD}")
        fig.write_html(OUTPUT_DASHBOARD)
        logging.info("✅ Operation Successful. BI Dashboard is live.")

if __name__ == "__main__":
    print("🚀 AssetSentinel: Interactive Insight Engine Online")
    engine = DashboardEngine(SOURCE_FILE)
    engine.compile_dashboard()
