"""
Web Intelligence Pro: Automated Entity Extraction Utility
---------------------------------------------------------
A robust, class-based scraping engine designed to identify, extract, 
and persist structured e-commerce data.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Automation
Date: February 2026
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import logging
from typing import List, Dict, Optional

# 1. Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class WebScraperEngine:
    def __init__(self, target_url: str):
        self.target_url: str = target_url
        self.headers: Dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }
        self.extracted_entities: List[Dict[str, str]] = []

    def fetch_dom_content(self) -> Optional[str]:
        """Initiates a network request and retrieves the raw HTML document."""
        logging.info(f"Connecting to target: {self.target_url}")
        try:
            response = requests.get(self.target_url, headers=self.headers, timeout=10)
            response.raise_for_status() # Raises an exception for HTTP errors (4xx, 5xx)
            logging.info("✅ Connection established. Proceeding to ingestion.")
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ Network Protocol Error: {e}")
            return None

    def parse_entities(self, html_content: str):
        """Parses the DOM and maps HTML elements to structured data dictionaries."""
        if not html_content:
            return

        soup = BeautifulSoup(html_content, "html.parser")
        products = soup.find_all("article", class_="product_pod")
        
        logging.info(f"Parsing active: {len(products)} entities identified.")

        for item in products:
            title = item.h3.a["title"]
            # Sanitizing price string: removing currency symbols and encoding artifacts
            price = item.find("p", class_="price_color").text.replace('Â', '')
            
            self.extracted_entities.append({
                'Item_Title': title,
                'Market_Price': price
            })
            logging.info(f"Synchronized: {title}")

    def persist_to_excel(self, output_filename: str):
        """Transforms extracted data into a structured Excel binary via Pandas."""
        if not self.extracted_entities:
            logging.warning("No data found for persistence.")
            return

        logging.info(f"Initializing persistence layer: Saving to {output_filename}")
        df = pd.DataFrame(self.extracted_entities)
        df.to_excel(output_filename, index=False)
        logging.info("🎉 Orchestration Complete. Deployment Successful.")

if __name__ == "__main__":
    # Deployment Parameters
    TARGET_SITE = "http://books.toscrape.com/"
    OUTPUT_FILE = "fiverr_market_intelligence.xlsx"

    # Execution Flow
    engine = WebScraperEngine(target_url=TARGET_SITE)
    raw_html = engine.fetch_dom_content()
    engine.parse_entities(raw_html)
    engine.persist_to_excel(output_filename=OUTPUT_FILE)
