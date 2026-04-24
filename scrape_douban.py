"""
CinemaOrchestrator Pro: Enterprise-Grade Web Harvesting Suite
--------------------------------------------------------------
A high-performance orchestration engine designed for resilient cinematic 
data acquisition, featuring session persistence and regex-based sanitization.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Intelligence
Date: April 20, 2026
"""

import re
import time
import random
import logging
import pandas as pd
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from requests import Session, adapters
from urllib3.util.retry import Retry
from typing import List, Dict, Final, Optional

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.FileHandler("harvest_audit.log"), logging.StreamHandler()]
)

class CinemaOrchestrator:
    def __init__(self, depth: int = 3):
        self.base_node: Final[str] = "https://movie.douban.com/top250"
        self.depth: int = depth
        self.vault_path: Final[Path] = Path("Vault/Cinema_Intelligence")
        self.registry: List[Dict] = []
        
        # Initialize resilient session with automated retry protocols
        self.session = self._initialize_resilient_session()
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the local persistence layer for secure storage."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"🛠️ Orchestration environment synchronized at: {self.vault_path.resolve()}")

    def _initialize_resilient_session(self) -> Session:
        """Configures a professional HTTP session with exponential backoff retries."""
        session = Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Referer": "https://movie.douban.com/"
        })
        
        # Exponential backoff retry strategy for handling network instability
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        adapter = adapters.HTTPAdapter(max_retries=retries)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _fetch_node_payload(self, index: int) -> Optional[str]:
        """Initiates a secure handshake and retrieves the raw DOM payload."""
        url = f"{self.base_node}?start={index}"
        logging.info(f"📡 Establishing connection to Node: {url}")
        
        try:
            # Adaptive Throttling: Humanizing the request interval
            time.sleep(random.uniform(2.0, 4.5))
            
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"❌ Handshake failure: {e}")
            return None

    def _parse_intelligence(self, html: str):
        """Orchestrates DOM parsing and executes regex-based data transformation."""
        if not html: return

        soup = BeautifulSoup(html, "html.parser")
        nodes = soup.find_all("div", class_="item")

        for node in nodes:
            try:
                title = node.find("span", class_="title").get_text()
                rating = node.find("span", class_="rating_num").get_text()
                
                # Regex Extraction: Precisely identifying numeric count from complex strings
                # e.g., "123456人评价" -> "123456"
                raw_stars = node.find(string=re.compile(r"\d+人评价"))
                review_count = re.search(r"\d+", raw_stars).group() if raw_stars else "0"

                self.registry.append({
                    "Sync_Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Movie_Title": title,
                    "Rating_Score": float(rating),
                    "Total_Reviews": int(review_count)
                })
                logging.info(f"   ✅ Synchronized: {title}")
            except (AttributeError, TypeError) as e:
                logging.warning(f"⚠️ Parsing anomaly detected: {e}")

    def execute_harvest(self):
        """Orchestrates the multi-stage ingestion lifecycle."""
        logging.info("🚀 CinemaIntelligence Sequence: ONLINE")
        
        for p in range(self.depth):
            start_ptr = p * 25
            payload = self._fetch_node_payload(start_ptr)
            self._parse_intelligence(payload)

        logging.info(f"🎉 Sequence Complete. {len(self.registry)} entities in registry.")

    def deploy_to_vault(self):
        """Persists the acquired intelligence into a structured Excel binary."""
        if not self.registry:
            logging.error("Deployment aborted: No valid entities in registry.")
            return

        filename = self.vault_path / f"Douban_Top_{len(self.registry)}_{datetime.now().strftime('%Y%m%d')}.xlsx"
        
        df = pd.DataFrame(self.registry)
        # Sorting by rating for immediate strategic insight
        df = df.sort_values(by="Rating_Score", ascending=False)
        
        df.to_excel(filename, index=False)
        logging.info(f"🏆 Strategic Asset persisted at: {filename}")

if __name__ == "__main__":
    # Operational Parameters: 2026 Market Standard
    print("\n" + "="*55)
    print("      YANG-TECH-LAB: CINEMA ORCHESTRATOR PRO")
    print("="*55 + "\n")
    
    orchestrator = CinemaOrchestrator(depth=3)
    orchestrator.execute_harvest()
    orchestrator.deploy_to_vault()
