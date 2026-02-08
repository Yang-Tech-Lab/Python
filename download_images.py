"""
MediaScraper Pro: Automated Asset Acquisition Utility
-----------------------------------------------------
A high-performance scraping engine designed to identify, resolve, 
and persist static web assets into structured local storage.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Automation
Date: February 2026
"""

import requests
import os
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List, Final

# 1. Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class AssetScraper:
    def __init__(self, target_url: str, storage_dir: str = "Static_Assets"):
        self.target_url: Final[str] = target_url
        self.storage_dir: Final[str] = storage_dir
        self._initialize_environment()

    def _initialize_environment(self):
        """Ensures the persistence layer (folder) is initialized."""
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)
            logging.info(f"Directory initialized: {self.storage_dir}")

    def fetch_resource_map(self) -> List[str]:
        """Parses the target DOM to extract image source attributes."""
        logging.info(f"Initiating connection to: {self.target_url}")
        try:
            response = requests.get(self.target_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            # Identifying assets by specific CSS class selectors
            images = soup.find_all("img", class_="thumbnail")
            
            # Resolving relative paths to absolute URLs
            urls = [urljoin(self.target_url, img['src']) for img in images]
            logging.info(f"Discovery complete. {len(urls)} assets identified.")
            return urls
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Network protocol error: {e}")
            return []

    def execute_download_sequence(self):
        """Orchestrates the binary stream acquisition and storage."""
        asset_urls = self.fetch_resource_map()
        
        for index, url in enumerate(asset_urls, start=1):
            try:
                logging.info(f"Acquiring asset {index}: {url}")
                # Fetching binary data stream
                asset_content = requests.get(url, timeout=10).content
                
                # Persistence logic: Saving as binary file
                file_path = os.path.join(self.storage_dir, f"asset_cover_{index}.jpg")
                with open(file_path, "wb") as f:
                    f.write(asset_content)
                    
            except Exception as e:
                logging.error(f"Failed to acquire asset {index} from {url}: {e}")

        logging.info("-" * 40)
        logging.info(f"Operation successful. Assets persisted in [{self.storage_dir}]")

if __name__ == "__main__":
    # Target: Sandbox environment for web scraping practice
    TARGET_SITE = "http://books.toscrape.com/"
    
    print("🚀 AssetSentinel: Media Acquisition Engine Online")
    engine = AssetScraper(target_url=TARGET_SITE)
    engine.execute_download_sequence()
