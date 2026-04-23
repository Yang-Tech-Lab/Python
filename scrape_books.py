"""
DataOrchestrator Pro: v6.2 Enterprise Edition
---------------------------------------------
An industrial-grade, context-aware ingestion engine designed for 
deterministic entity extraction and high-fidelity persistence.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Industrial Automation
Date: April 22, 2026
"""

import logging
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Final, Any
from requests import Session, adapters
from urllib3.util.retry import Retry

# 1. Industrial Infrastructure Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("Vault/Logs/ingestion_audit.log"),
        logging.StreamHandler()
    ]
)

@dataclass(frozen=True)
class MarketEntity:
    """Immutable data schema for strategic market assets."""
    title: str
    valuation_gbp: float
    sync_timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class DataOrchestrator:
    def __init__(self, target_node: str):
        self.target_node: Final[str] = target_node
        self.vault_path: Final[Path] = Path("Vault/Intelligence")
        self.registry: List[MarketEntity] = []
        self.session: Optional[Session] = None
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure data vault and audit layers."""
        self.vault_path.mkdir(parents=True, exist_ok=True)
        Path("Vault/Logs").mkdir(parents=True, exist_ok=True)
        logging.info(f"🛠️ Node Environment Synchronized: {self.vault_path.resolve()}")

    def __enter__(self):
        """Initializes the resilient HTTP session context."""
        self.session = Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        })
        
        # 2026 Strategy: Exponential backoff for handling network jitter
        retries = Retry(total=5, backoff_factor=1.5, status_forcelist=[500, 502, 503, 504])
        adapter = adapters.HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=10)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Safely decommissions the session and releases network handles."""
        if self.session:
            self.session.close()
            logging.info("🏁 Sentinel Protocol Offline. Resources released.")

    def ingest_raw_payload(self) -> Optional[str]:
        """Initiates a secure handshake and retrieves the DOM telemetry."""
        logging.info(f"📡 Synchronizing with Node: {self.target_node}")
        try:
            response = self.session.get(self.target_node, timeout=15)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"❌ Handshake Failure: {e}")
            return None

    def transform_payload(self, html_content: str):
        """Orchestrates DOM parsing and executes non-linear data transformation."""
        if not html_content: return

        soup = BeautifulSoup(html_content, "html.parser")
        nodes = soup.select("article.product_pod")
        
        logging.info(f"Analyzing {len(nodes)} detected entities.")

        for node in nodes:
            try:
                title = node.h3.a["title"]
                price_text = node.select_one("p.price_color").text
                # Precision cleaning logic
                price_numeric = float(''.join(c for c in price_text if c.isdigit() or c == '.'))
                
                self.registry.append(MarketEntity(
                    title=title,
                    valuation_gbp=price_numeric
                ))
            except Exception as e:
                logging.warning(f"⚠️ Telemetry Anomaly: {e}")

    def deploy_to_vault(self):
        """Persists the acquired intelligence to a structured Excel binary."""
        if not self.registry:
            logging.error("Deployment aborted: Registry is null.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        target_file = self.vault_path / f"Market_Intel_{timestamp}.xlsx"
        
        # Data Transformation for persistence
        df = pd.DataFrame([asdict(entity) for entity in self.registry])
        
        try:
            df.to_excel(target_file, index=False)
            logging.info(f"🏆 Strategic Asset Persisted: {target_file.name}")
        except Exception as e:
            logging.error(f"❌ Persistence Breach: {e}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("      YANG-TECH-LAB: DATA ORCHESTRATOR PRO v6.2")
    print("="*60 + "\n")
    
    TARGET_GRID = "http://books.toscrape.com/"

    # Using Context Manager for guaranteed resource orchestration
    with DataOrchestrator(target_node=TARGET_GRID) as orchestrator:
        raw_data = orchestrator.ingest_raw_payload()
        orchestrator.transform_payload(raw_data)
        orchestrator.deploy_to_vault()
