"""
VisualIntelligence Pro: High-Fidelity Analytics Orchestrator
-----------------------------------------------------------
An enterprise-grade visualization engine designed to transform raw 
financial datasets into executive-level strategic reports.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Intelligence / Data Engineering
Date: March 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import logging
import sys
from pathlib import Path
from typing import Final, Tuple, Optional

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class VisualIntelligenceOrchestrator:
    def __init__(self, source_name: str = 'fiverr_report_finished.xlsx'):
        self.source_path: Final[Path] = Path(source_name)
        self.output_path: Final[Path] = Path('Vault/Strategic_Analytics_2026.png')
        self.brand_color: Final[str] = '#2E86C1'  # Professional Slate Blue
        self.accent_color: Final[str] = '#1B4F72' # Deep Navy
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the local persistence layer for asset storage."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        logging.info("🛠️ Visualization environment synchronized.")

    def _ingest_and_refine_data(self) -> pd.DataFrame:
        """Loads data and applies strategic sorting for maximum insight."""
        logging.info(f"Ingesting data from: {self.source_path}")
        try:
            df = pd.read_excel(self.source_path)
            # Strategy: Sort by revenue to provide immediate Pareto-style insight
            return df.sort_values(by='销售总额', ascending=False)
        except Exception as e:
            logging.error(f"❌ Ingestion failure: {e}")
            sys.exit(1)

    def render_strategic_visual(self, df: pd.DataFrame):
        """Orchestrates the rendering of a high-fidelity bar analytics chart."""
        logging.info("Initializing high-fidelity rendering pipeline...")
        
        # 2. Canvas Configuration (Object-Oriented API)
        plt.style.use('seaborn-v0_8-muted') # 2026 Standard for clean BI visuals
        fig, ax = plt.subplots(figsize=(14, 8), dpi=300) # Ultra-high definition

        # 3. Core Rendering Logic
        bars = ax.bar(
            df['产品名称'], 
            df['销售总额'], 
            color=self.brand_color, 
            edgecolor=self.accent_color, 
            alpha=0.9,
            linewidth=1.2
        )

        # 4. Metadata & Precision Labeling
        ax.set_title('Strategic Revenue Analysis by Product Line', fontsize=20, fontweight='bold', pad=30)
        ax.set_xlabel('Product Category', fontsize=14, labelpad=15)
        ax.set_ylabel('Aggregated Revenue (USD)', fontsize=14, labelpad=15)
        
        # Precision Data Annotation
        for bar in bars:
            yval = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                yval + (yval * 0.01), 
                f'${yval:,.0f}', 
                ha='center', va='bottom', 
                fontsize=11, fontweight='bold',
                color=self.accent_color
            )

        # 5. Aesthetic Refinement
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', linestyle='--', alpha=0.4)
        plt.xticks(rotation=45, ha='right', fontsize=11)

        # 6. Persistence Layer
        plt.tight_layout()
        logging.info(f"Persisting strategic asset to: {self.output_path}")
        fig.savefig(self.output_path, bbox_inches='tight')
        plt.close(fig)

    def execute_pipeline(self):
        """Orchestrates the full data-to-visual intelligence lifecycle."""
        print("\n" + "="*55)
        print("      YANG-TECH-LAB: VISUAL INTELLIGENCE PRO")
        print("="*55 + "\n")
        
        data = self._ingest_and_refine_data()
        self.render_strategic_visual(data)
        
        logging.info("🏆 Operation Successful. Strategic visual asset is live.")

if __name__ == "__main__":
    orchestrator = VisualIntelligenceOrchestrator()
    orchestrator.execute_pipeline()
