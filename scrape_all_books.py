"""
Multi-Page Data Extraction Engine
---------------------------------
A professional-grade web scraper designed for robust, multi-page data 
acquisition and structured persistence.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Automation
Date: February 2026
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import logging
from typing import List, Dict, Final

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class DataExtractionEngine:
    def __init__(self, base_url: str, total_pages: int):
        self.base_url: Final[str] = base_url
        self.total_pages: Final[int] = total_pages
        self.headers: Dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }
        self.extracted_data: List[Dict] = []

    def _fetch_page_content(self, page_num: int) -> str:
        """Executes a GET request to the target URL with error handling."""
        url = f"{self.base_url}/catalogue/page-{page_num}.html"
        logging.info(f"Initiating connection to Page {page_num}...")
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Network Protocol Error on Page {page_num}: {e}")
            return ""

    def _parse_raw_data(self, html_content: str, page_num: int):
        """Parses the DOM and extracts specific entity attributes."""
        if not html_content:
            return

        soup = BeautifulSoup(html_content, "html.parser")
        product_pods = soup.find_all("article", class_="product_pod")

        for pod in product_pods:
            title = pod.h3.a["title"]
            price = pod.find("p", class_="price_color").text.replace('Â', '')
            
            self.extracted_data.append({
                'Origin_Page': page_num,
                'Item_Title': title,
                'Unit_Price': price
            })

    def run_acquisition_pipeline(self):
        """Orchestrates the full extraction workflow with throttling logic."""
        logging.info("🚀 Data Acquisition Pipeline Started.")
        
        for i in range(1, self.total_pages + 1):
            content = self._fetch_page_content(i)
            self._parse_raw_data(content, i)
            
            # Implementation of Throttling (Rate Limiting) to ensure crawler persistence
            # This simulates human browsing behavior
            time.sleep(1.2)

        logging.info(f"✅ Acquisition Complete. Total records identified: {len(self.extracted_data)}")

    def persist_to_excel(self, filename: str = "fiverr_books_all.xlsx"):
        """Saves the extracted dataset into a structured Excel spreadsheet."""
        if not self.extracted_data:
            logging.warning("No data found to persist.")
            return

        df = pd.DataFrame(self.extracted_data)
        df.to_excel(filename, index=False)
        logging.info(f"📂 Strategic Asset persisted at: [{filename}]")

if __name__ == "__main__":
    # Deployment Parameters
    TARGET_SITE = "http://books.toscrape.com"
    PAGE_COUNT = 5

    # Execute Engine
    engine = DataExtractionEngine(base_url=TARGET_SITE, total_pages=PAGE_COUNT)
    engine.run_acquisition_pipeline()
    engine.persist_to_excel()
