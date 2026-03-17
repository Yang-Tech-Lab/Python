"""
IngestionEngine Pro: Enterprise Data Acquisition Suite
-------------------------------------------------------
A high-performance, resilient orchestration engine designed for 
automated entity extraction and strategic data persistence.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Systems Automation
Date: March 2026
"""

import logging
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Final
from requests import Session, adapters
from urllib3.util.retry import Retry

# 1. Industrial Logging Configuration (Log to both console and file)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("ingestion_audit.log"),
        logging.StreamHandler()
    ]
)

class IngestionEngine:
    def __init__(self, target_node: str):
        self.target_node: Final[str] = target_node
        self.vault_path: Final[Path] = Path("Vault/Intelligence")
        self.registry: List[Dict[str, str]] = []
        
        # Initialize resilient session with automated retry protocols
        self.session = self._initialize_resilient_session()
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure data vault for persistence."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"🛠️ Environment synchronized at: {self.vault_path.resolve()}")

    def _initialize_resilient_session(self) -> Session:
        """Configures a professional HTTP session with exponential backoff retries."""
        session = Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        })
        
        # Retry logic: 5 retries on 502, 503, 504 with backoff factor
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        adapter = adapters.HTTPAdapter(max_retries=retries)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def fetch_strategic_data(self) -> Optional[str]:
        """Initiates a secure handshake and retrieves the raw DOM payload."""
        logging.info(f"📡 Establishing connection to node: {self.target_node}")
        try:
            response = self.session.get(self.target_node, timeout=12)
            response.raise_for_status()
            logging.info("✅ Handshake successful. Data ingestion initiated.")
            return response.text
        except Exception as e:
            logging.error(f"❌ Connection Breach: {e}")
            return None

    def transform_dom_to_entities(self, html_content: str):
        """Orchestrates DOM parsing and executes data transformation logic."""
        if not html_content:
            return

        soup = BeautifulSoup(html_content, "html.parser")
        product_nodes = soup.find_all("article", class_="product_pod")
        
        logging.info(f"Analyzing {len(product_nodes)} detected entities.")

        for node in product_nodes:
            try:
                title = node.h3.a["title"]
                price_raw = node.find("p", class_="price_color").text
                # Advanced sanitization: targeting numeric precision
                price_clean = price_raw.replace('£', '').replace('Â', '').strip()
                
                self.registry.append({
                    'Entity_ID': title,
                    'Market_Value': price_clean,
                    'Sync_Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            except (AttributeError, KeyError) as e:
                logging.warning(f"⚠️ Parsing anomaly detected for an entity: {e}")

    def deploy_to_vault(self, filename: str):
        """Persists the acquired intelligence to a structured Excel binary."""
        if not self.registry:
            logging.error("Deployment aborted: No valid entities in the registry.")
            return

        target_file = self.vault_path / filename
        logging.info(f"💾 Persisting strategic assets to: {target_file}")
        
        df = pd.DataFrame(self.registry)
        df.to_excel(target_file, index=False)
        logging.info("🏆 Operation Accomplished. System returning to standby.")

if __name__ == "__main__":
    # Operational Parameters
    TARGET_GRID = "http://books.toscrape.com/"
    OUTPUT_ASSET = f"Market_Intelligence_{datetime.now().strftime('%Y%m%d')}.xlsx"

    # Execution Sequence
    engine = IngestionEngine(target_node=TARGET_GRID)
    payload = engine.fetch_strategic_data()
    engine.transform_dom_to_entities(payload)
    engine.deploy_to_vault(filename=OUTPUT_ASSET)
