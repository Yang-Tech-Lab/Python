"""
VisualOrchestrator Pro: Executive Decision Support Engine
---------------------------------------------------------
A high-fidelity visualization node designed for deterministic market 
analysis, leveraging Pareto distribution for strategic insight.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Intelligence / Systems Engineering
Date: April 13, 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from pathlib import Path
from datetime import datetime
from typing import Final, Optional, Tuple

# 1. Industrial Infrastructure Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("Vault/Logs/visual_audit.log"),
        logging.StreamHandler()
    ]
)

class VisualOrchestrator:
    def __init__(self, source_node: str = "fiverr_report_finished.xlsx"):
        self.source_path: Final[Path] = Path(source_node)
        self.vault_path: Final[Path] = Path("Vault/Strategic_Assets")
        self.brand_navy: Final[str] = "#1B2631"  # Deep Charcoal
        self.success_green: Final[str] = "#27AE60" # Emerald Profit
        
        self._bootstrap_environment()
        self._configure_typography()

    def _bootstrap_environment(self):
        """Provisions the secure local storage and audit layers."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        Path("Vault/Logs").mkdir(parents=True, exist_ok=True)
        logging.info("🛠️ Orchestration vault synchronized.")

    def _configure_typography(self):
        """Standardizes font rendering for international/Chinese characters."""
        # 2026 Standard: High-fidelity font rendering
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False
        sns.set_theme(style="whitegrid", font='SimHei')
        logging.info("🖋️ Typography engine optimized for CJK characters.")

    def _ingest_and_calculate_pareto(self) -> pd.DataFrame:
        """Loads raw telemetry and computes Pareto cumulative metrics."""
        logging.info(f"Ingesting market data from: {self.source_path.name}")
        try:
            df = pd.read_excel(self.source_path)
            # Strategy: Sorting by primary fiscal metric
            df = df.sort_values(by='销售总额', ascending=False).reset_index(drop=True)
            
            # Calculating Cumulative Contribution (80/20 Rule)
            df['Cumulative_Pct'] = (df['销售总额'].cumsum() / df['销售总额'].sum()) * 100
            return df
        except Exception as e:
            logging.error(f"❌ Ingestion Breach: {e}")
            raise

    def synthesize_executive_asset(self):
        """Orchestrates the synthesis of a high-fidelity Pareto analytics chart."""
        df = self._ingest_and_calculate_pareto()
        
        # Canvas Orchestration (Object-Oriented API)
        fig, ax1 = plt.subplots(figsize=(16, 9), dpi=300)
        
        # --- Layer 1: Absolute Revenue Bar Chart ---
        bars = ax1.bar(
            df['产品名称'], df['销售总额'], 
            color=self.brand_navy, alpha=0.85, label='Aggregated Revenue'
        )
        ax1.set_ylabel('Revenue (USD)', fontsize=12, fontweight='bold', color=self.brand_navy)
        
        # --- Layer 2: Cumulative Percentage Curve ---
        ax2 = ax1.twinx()
        ax2.plot(
            df['产品名称'], df['Cumulative_Pct'], 
            color=self.success_green, marker='D', markersize=8, 
            linewidth=2.5, label='Cumulative %'
        )
        ax2.set_ylabel('Cumulative Contribution (%)', fontsize=12, fontweight='bold', color=self.success_green)
        ax2.set_ylim(0, 110)

        # --- Layer 3: Annotations & Metadata ---
        ax1.set_title(f"Strategic Asset Analysis: {datetime.now().year} Portfolio", fontsize=22, fontweight='bold', pad=30)
        
        # Labeling the bars with precision metrics
        for bar in bars:
            height = bar.get_height()
            ax1.text(
                bar.get_x() + bar.get_width()/2., height + (height * 0.02),
                f'${height:,.0f}', ha='center', va='bottom', 
                fontsize=10, fontweight='bold', color=self.brand_navy
            )

        # Visual Grid Refinement
        ax1.set_xticklabels(df['产品名称'], rotation=40, ha='right', fontsize=11)
        ax1.grid(axis='y', linestyle='--', alpha=0.4)
        
        # Persistence Layer (PNG for fast ingestion, PDF for client delivery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        export_base = self.vault_path / f"Executive_Insight_{timestamp}"
        
        plt.tight_layout()
        fig.savefig(f"{export_base}.png", bbox_inches='tight')
        logging.info(f"🏆 Strategic asset persisted: {export_base}.png")
        plt.close(fig)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("      YANG-TECH-LAB: VISUAL INTELLIGENCE PRO v5.2")
    print("="*60 + "\n")
    
    try:
        orchestrator = VisualOrchestrator(source_node='fiverr_report_finished.xlsx')
        orchestrator.synthesize_executive_asset()
    except Exception as fatal_e:
        logging.critical(f"System Crash during orchestration: {fatal_e}")
    
    print("\n--- Synthesis Cycle Complete: Intelligence Asset Live ---")
