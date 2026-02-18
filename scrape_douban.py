"""
CinemaIntelligence Pro: Advanced Web Harvesting Engine
------------------------------------------------------
A professional-grade scraping utility designed to extract, sanitize, 
and persist top-tier cinematic data from dynamic web environments.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Market Intelligence
Date: February 2026
"""

import requests
import pandas as pd
import logging
import time
import random
from bs4 import BeautifulSoup
from typing import List, Dict, Final

# 1. Professional Logging & Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class DoubanScraper:
    def __init__(self, target_pages: int = 3):
        self.base_url: Final[str] = "https://movie.douban.com/top250"
        self.target_pages: int = target_pages
        # User-Agent Spoofing to bypass basic anti-bot mechanisms
        self.headers: Dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }
        self.movie_registry: List[Dict] = []

    def _fetch_dom(self, start_index: int) -> str:
        """Executes a network request to retrieve the raw HTML payload."""
        url = f"{self.base_url}?start={start_index}"
        logging.info(f"Initiating handshake with: {url}")
        
        try:
            response = requests.get(url, headers=self.headers, timeout=12)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Network Protocol Breach: {e}")
            return ""

    def _parse_and_sanitize(self, html_content: str):
        """Parses the DOM and performs data sanitization on extracted attributes."""
        if not html_content:
            return

        soup = BeautifulSoup(html_content, "html.parser")
        items = soup.find_all("div", class_="item")

        for item in items:
            try:
                title = item.find("span", class_="title").get_text()
                rating = item.find("span", class_="rating_num").get_text()
                
                # Extracting count and sanitizing non-numeric characters
                # Converting '12345人评价' to raw integer string
                review_count_raw = item.find_all("span")[-2].get_text()
                review_count = review_count_raw.replace("人评价", "").strip()

                self.movie_registry.append({
                    "Movie_Title": title,
                    "Rating_Score": rating,
                    "Total_Reviews": review_count
                })
                logging.info(f"Synchronized: {title} (Rating: {rating})")
            except AttributeError as e:
                logging.warning(f"Attribute mismatch during parsing: {e}")

    def execute_harvest_sequence(self):
        """Orchestrates the multi-page extraction workflow with randomized throttling."""
        logging.info("🚀 CinemaIntelligence Sequence Initiated.")
        
        for p in range(self.target_pages):
            start_index = p * 25
            logging.info(f"Processing Page {p + 1}...")
            
            payload = self._fetch_dom(start_index)
            self._parse_and_sanitize(payload)

            # Adaptive Throttling: Simulates human browsing latency to prevent IP blacklisting
            # Critical for maintaining a professional crawler's reputation
            delay = random.uniform(1.5, 3.5)
            time.sleep(delay)

        logging.info(f"✅ Harvest Complete. {len(self.movie_registry)} entities persisted.")

    def export_dataset(self, filename: str = "douban_intelligence_top75.xlsx"):
        """Transforms the registry into a structured Excel spreadsheet (Persistence Layer)."""
        if not self.movie_registry:
            logging.warning("No data detected. Aborting export.")
            return

        df = pd.DataFrame(self.movie_registry)
        df.to_excel(filename, index=False)
        logging.info(f"📂 Strategic Asset persisted at: [{filename}]")

if __name__ == "__main__":
    # Initialize Engine with a target of 3 pages (75 movies)
    engine = DoubanScraper(target_pages=3)
    engine.execute_harvest_sequence()
    engine.export_dataset()
