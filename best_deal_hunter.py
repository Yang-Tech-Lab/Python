"""
MarketIntel Pro: High-Fidelity Scraper & Report Generator
---------------------------------------------------------
An enterprise-ready discovery engine designed to identify retail 
arbitrage opportunities through structured data ingestion.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Automation / Business Intelligence
Date: March 2026
"""

import time
import random
import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup
from docx import Document
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Final, Optional

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class MarketScanner:
    def __init__(self, page_limit: int = 10):
        self.page_limit: Final[int] = page_limit
        self.base_url: Final[str] = "http://books.toscrape.com/catalogue/page-{}.html"
        self.headers: Final[Dict[str, str]] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Referer": "https://www.google.com/"
        }
        self.rating_map: Final[Dict[str, int]] = {
            "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
        }
        self.premium_inventory: List[Dict] = []

    def _apply_throttling(self):
        """Simulates human-like latency between requests."""
        delay = random.uniform(1.8, 4.2)
        time.sleep(delay)

    def fetch_page_data(self, page_index: int) -> Optional[BeautifulSoup]:
        """Handshakes with the target node and returns the parsed DOM."""
        url = self.base_url.format(page_index)
        logging.info(f"Connecting to Node: {url}")
        
        try:
            self._apply_throttling()
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException as e:
            logging.error(f"Network Protocol Breach on Page {page_index}: {e}")
            return None

    def execute_scan(self):
        """Orchestrates the multi-page acquisition sequence."""
        logging.info("🚀 Initiating Market Surveillance Protocol...")
        
        for p in range(1, self.page_limit + 1):
            soup = self.fetch_page_data(p)
            if not soup: continue

            books = soup.find_all("article", class_="product_pod")
            for book in books:
                # Extracting categorical data
                star_class = book.find("p", class_="star-rating")["class"][1]
                rating = self.rating_map.get(star_class, 0)
                
                price_text = book.find("p", class_="price_color").text
                price = float(price_text.replace("£", "").replace("Â", ""))

                # Filtering Logic (Strategic Arbitrage)
                # Requirement: Max Rating & Competitive Price
                if rating == 5 and price < 20.0:
                    title = book.h3.a["title"]
                    logging.info(f"   💰 Strategic Match Identified: {title}")
                    self.premium_inventory.append({
                        "Title": title,
                        "Price_GBP": price,
                        "Rating": "⭐⭐⭐⭐⭐"
                    })

    def generate_professional_report(self):
        """Persists the acquired intelligence into a branded Word deliverable."""
        if not self.premium_inventory:
            logging.warning("Deployment aborted: No high-value assets identified.")
            return

        logging.info("📝 Compiling Executive Market Intelligence Report...")
        doc = Document()
        doc.add_heading('Commercial Market Intelligence Report', 0)
        
        # Meta Metadata
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        doc.add_paragraph(f"Auditor: Yang's Automation Engine | Sync Date: {timestamp}")
        doc.add_paragraph("Analysis Focus: 5-Star Rated Assets with Optimal Price-Point (< £20)")

        # Table Orchestration
        table = doc.add_table(rows=1, cols=3)
        table.style = 'Table Grid'
        
        # Header Setup
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text, hdr_cells[1].text, hdr_cells[2].text = 'Item Identifier', 'Price (£)', 'Rating'

        for item in self.premium_inventory:
            row = table.add_row().cells
            row[0].text = item['Title']
            row[1].text = f"£{item['Price_GBP']}"
            row[2].text = item['Rating']

        filename = f"Market_Intelligence_{datetime.now().strftime('%Y%m%d')}.docx"
        doc.save(filename)
        logging.info(f"🏆 Deliverable synthesized: {filename}")

if __name__ == "__main__":
    # Standard Operating Procedure (SOP)
    scanner = MarketScanner(page_limit=10)
    scanner.execute_scan()
    scanner.generate_professional_report()
