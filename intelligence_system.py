"""
MarketIntel Pro: Automated Competitor Intelligence & Strategic Reporting
-----------------------------------------------------------------------
An enterprise-grade analytics engine that monitors competitor pricing, 
visualizes trends, and generates AI-driven strategic PDF reports.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Business Intelligence / Automation
Date: February 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
import logging
from datetime import datetime
from typing import Final

# 1. Professional Logging & Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')

class IntelligenceEngine:
    def __init__(self, data_source: str = "competitor_data.csv"):
        self.data_source: Final[str] = data_source
        self.report_date: Final[str] = datetime.now().strftime('%Y-%m-%d')
        self.output_pdf: Final[str] = f"Market_Intelligence_Report_{self.report_date}.pdf"
        self.page_width, self.page_height = LETTER

    def load_market_data(self) -> pd.DataFrame:
        """Loads and validates competitor datasets."""
        if not os.path.exists(self.data_source):
            logging.error(f"Critical Error: Data source '{self.data_source}' not found.")
            return pd.DataFrame()
        return pd.read_csv(self.data_source)

    def generate_trend_chart(self, product_name: str, data: pd.DataFrame) -> str:
        """Visualizes price trends and returns the temporary image path."""
        plt.style.use('ggplot')  # Professional styling
        plt.figure(figsize=(6, 3))
        
        plt.plot(data['Date'], data['Competitor_Price'], marker='s', color='#E74C3C', linestyle='-', linewidth=2)
        plt.title(f"Strategic Analysis: {product_name}", fontsize=12, fontweight='bold')
        plt.xlabel("Timeline", fontsize=9)
        plt.ylabel("Price (USD)", fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        temp_path = f"temp_viz_{product_name}.png"
        plt.savefig(temp_path, dpi=150)
        plt.close()
        return temp_path

    def compile_strategic_report(self):
        """Orchestrates the data analysis and PDF compilation sequence."""
        df = self.load_market_data()
        if df.empty: return

        logging.info("Initiating intelligence compilation sequence...")
        c = canvas.Canvas(self.output_pdf, pagesize=LETTER)
        
        # --- PDF Header Section ---
        c.setFont("Helvetica-Bold", 22)
        c.drawString(50, 750, "Market Surveillance & Strategic Report")
        c.setFont("Helvetica", 10)
        c.drawString(50, 730, f"Confidential Intelligence | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        c.setStrokeColorRGB(0.1, 0.1, 0.4)
        c.line(50, 720, 560, 720)

        cursor_y = 680
        products = df['Product'].unique()

        for product in products:
            logging.info(f"Analyzing product: {product}")
            prod_data = df[df['Product'] == product]
            
            # Financial Calculations
            curr_price = prod_data.iloc[-1]['Competitor_Price']
            unit_cost = prod_data.iloc[-1]['My_Cost']
            margin_pct = ((curr_price - unit_cost) / curr_price) * 100

            # Page Management
            if cursor_y < 280:
                c.showPage()
                cursor_y = 750

            # --- Technical Content Injection ---
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, cursor_y, f"Portfolio Item: {product}")
            
            c.setFont("Helvetica", 11)
            c.drawString(50, cursor_y - 25, f"Latest Market Valuation: ${curr_price:,.2f}")
            c.drawString(50, cursor_y - 40, f"Operational Margin: {margin_pct:.2f}%")

            # AI Logic Implementation
            if margin_pct < 20:
                c.setFillColorRGB(0.75, 0, 0) # Alert Red
                advice = "ADVISORY: Critical margin. Price reduction prohibited."
            else:
                c.setFillColorRGB(0, 0.4, 0) # Strategic Green
                advice = "OPPORTUNITY: High liquidity. Aggressive pricing recommended."
            
            c.setFont("Helvetica-BoldOblique", 10)
            c.drawString(50, cursor_y - 60, f"Strategic Advice: {advice}")
            c.setFillColorRGB(0, 0, 0)

            # Chart Integration
            chart_path = self.generate_trend_chart(product, prod_data)
            c.drawImage(ImageReader(chart_path), 280, cursor_y - 120, width=280, height=140)
            os.remove(chart_path)

            cursor_y -= 180
            c.setDash(1, 2)
            c.line(50, cursor_y + 15, 560, cursor_y + 15)
            c.setDash(1, 0)

        c.save()
        logging.info(f"Report Successfully Compiled: {self.output_pdf}")

if __name__ == "__main__":
    engine = IntelligenceEngine()
    engine.compile_strategic_report()
