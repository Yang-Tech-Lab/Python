"""
SalesData Visualization Engine Pro
----------------------------------
A professional-grade analytics utility that transforms processed Excel data 
into high-fidelity visual intelligence reports.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Intelligence
Date: February 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import logging
from typing import Final

# 1. Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

# Constants for easy maintenance
SOURCE_FILE: Final[str] = 'fiverr_report_finished.xlsx'
OUTPUT_IMAGE: Final[str] = 'sales_performance_analytics.png'

def execute_visualization_pipeline():
    logging.info("🚀 Initializing Visualization Pipeline...")

    try:
        # 2. Data Ingestion
        logging.info(f"Ingesting processed records from: {SOURCE_FILE}")
        df = pd.read_excel(SOURCE_FILE)

        # 3. Canvas Initialization & Styling
        # Using a modern style for a professional "Software-as-a-Service" aesthetic
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(12, 7))

        # 4. Core Rendering Logic
        logging.info("Rendering categorical bar chart...")
        bars = ax.bar(df['产品名称'], df['销售总额'], color='#3498db', edgecolor='#2980b9', alpha=0.85)

        # 5. Metadata & Labeling (International Standards)
        ax.set_title('Revenue Analysis by Product Category', fontsize=18, fontweight='bold', pad=20)
        ax.set_xlabel('Product Line', fontsize=13, labelpad=10)
        ax.set_ylabel('Total Revenue (USD)', fontsize=13, labelpad=10)
        
        # Adding data labels on top of bars for immediate insight
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f'${yval:,.0f}', 
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

        # 6. Persistence Layer
        plt.tight_layout()
        plt.savefig(OUTPUT_IMAGE, dpi=300) # 300 DPI for high-quality client deliverables
        logging.info(f"✅ Success! Strategic visual asset persisted at: [{OUTPUT_IMAGE}]")

    except FileNotFoundError:
        logging.error(f"❌ Critical Failure: '{SOURCE_FILE}' not found. Please verify data source.")
    except Exception as e:
        logging.error(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    execute_visualization_pipeline()
