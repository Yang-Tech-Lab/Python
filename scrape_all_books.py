"""
DataOrchestrator Pro: High-Fidelity Multi-Page Ingestion Suite
--------------------------------------------------------------
An enterprise-ready orchestration engine designed for resilient web 
data acquisition, featuring automated session retries and structured 
persistence for high-volume analytics.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Automation
Date: April 17，2026
"""

import time
import logging
import random
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Final, Optional
from requests import Session, adapters
from urllib3.util.retry import Retry

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("ingestion_audit.log"),
        logging.StreamHandler()
    ]
)

class DataOrchestrator:
    def __init__(self, base_node: str, page_limit: int):
        self.base_node: Final[str] = base_node
        self.page_limit: Final[int] = page_limit
        self.vault_path: Final[Path] = Path("Vault/Market_Intelligence")
        self.registry: List[Dict] = []
        
        # Initialize resilient session with automated retry protocols
        self.session = self._initialize_resilient_session()
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure data vault for persistent storage."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"🛠️ Ingestion environment synchronized at: {self.vault_path.resolve()}")

    def _initialize_resilient_session(self) -> Session:
        """Configures a professional HTTP session with exponential backoff retries."""
        session = Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        })
        
        # Logic: Retry on 502, 503, 504 with exponential backoff
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        adapter = adapters.HTTPAdapter(max_retries=retries)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _fetch_page_handshake(self, index: int) -> Optional[str]:
        """Initiates a secure handshake with the target node."""
        target_url = f"{self.base_node}/catalogue/page-{index}.html"
        logging.info(f"📡 Synchronizing with Node {index}: {target_url}")
        
        try:
            # Applying adaptive throttling to simulate human entropy
            time.sleep(random.uniform(1.5, 3.5))
            
            response = self.session.get(target_url, timeout=12)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"❌ Handshake failure on Node {index}: {e}")
            return None

    def _transform_raw_dom(self, html: str, node_id: int):
        """Parses the raw DOM and executes attribute extraction logic."""
        soup = BeautifulSoup(html, "html.parser")
        entities = soup.find_all("article", class_="product_pod")

        for entity in entities:
            # Data Cleaning: Extracting and refining metrics
            title = entity.h3.a["title"]
            price_raw = entity.find("p", class_="price_color").text
            price_clean = float(price_raw.replace('£', '').replace('Â', ''))
            
            self.registry.append({
                'Sync_Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Source_Node': node_id,
                'Asset_Identifier': title,
                'Market_Valuation_GBP': price_clean,
                'Currency': 'GBP'
            })

    def execute_ingestion_pipeline(self):
        """Orchestrates the full multi-stage data acquisition lifecycle."""
        logging.info("🚀 Data Ingestion Pipeline: ONLINE")
        
        for i in range(1, self.page_limit + 1):
            raw_content = self._fetch_page_handshake(i)
            if raw_content:
                self._transform_raw_dom(raw_content, i)
                logging.info(f"   ✅ Node {i} processed. Accumulated entities: {len(self.registry)}")
            else:
                logging.warning(f"   ⚠️ Skipping Node {i} due to connectivity breach.")

    def persist_to_excel(self):
        """Persists the acquired intelligence into a structured Excel binary."""
        if not self.registry:
            logging.error("Persistence Aborted: No data identifies in the registry.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = self.vault_path / f"Global_Intelligence_Pulse_{timestamp}.xlsx"
        
        df = pd.DataFrame(self.registry)
        df.to_excel(filename, index=False)
        logging.info(f"🏆 Mission Accomplished. Strategic asset persisted at: {filename}")

if __name__ == "__main__":
    # Deployment Parameters
    TARGET_GRID = "http://books.toscrape.com"
    SEARCH_DEPTH = 5

    print("\n" + "="*55)
    print("      YANG-TECH-LAB: DATA ORCHESTRATOR PRO")
    print("="*55 + "\n")
    
    engine = DataOrchestrator(base_node=TARGET_GRID, page_limit=SEARCH_DEPTH)
    engine.execute_ingestion_pipeline()
    engine.persist_to_excel()
