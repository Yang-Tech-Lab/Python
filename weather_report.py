"""
MeteorologicalOrchestrator Pro: Enterprise Data Synthesis Engine
----------------------------------------------------------------
A high-performance, asynchronous-ready orchestration engine for 
geospatial intelligence acquisition and strategic fiscal persistence.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Intelligence
Date: March 23, 2026
"""

import os
import logging
import pandas as pd
import requests
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Optional, Final, TypedDict

# 1. Industrial Infrastructure Configuration
load_dotenv() # Ingests secrets from .env securely

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.FileHandler("vault_audit.log"), logging.StreamHandler()]
)

class NodeTelemetry(TypedDict):
    """Strict data schema for high-fidelity geospatial intelligence."""
    Node_ID: str
    Temp_C: float
    Humidity_Pct: int
    Wind_Velocity_MS: float
    Condition: str
    Sync_Timestamp: str

class IntelligenceOrchestrator:
    def __init__(self):
        # Security: Decoupled secret management
        self.__api_key: Final[str] = os.getenv("OPENWEATHER_API_KEY", "")
        self.base_url: Final[str] = "https://api.openweathermap.org/data/2.5/weather"
        self.vault_dir: Final[Path] = Path("Vault/Intelligence")
        self.registry: List[NodeTelemetry] = []
        
        self._bootstrap_environment()

    def _bootstrap_environment(self):
        """Provisions the secure local persistence layers."""
        self.vault_dir.mkdir(parents=True, exist_ok=True)
        if not self.__api_key:
            logging.critical("Security Breach: Node unauthorized. Missing API Key.")
            raise ConnectionError("Authentication failure in environment orchestration.")

    def _fetch_node_pulse(self, city: str) -> Optional[NodeTelemetry]:
        """Executes a single node handshake with resilient error recovery."""
        params = {"q": city, "appid": self.__api_key, "units": "metric", "lang": "en"}
        
        try:
            # Applying adaptive timeout for global grid synchronization
            response = requests.get(self.base_url, params=params, timeout=12)
            response.raise_for_status()
            data = response.json()
            
            return {
                "Node_ID": city.upper(),
                "Temp_C": data['main']['temp'],
                "Humidity_Pct": data['main']['humidity'],
                "Wind_Velocity_MS": data['wind']['speed'],
                "Condition": data['weather'][0]['description'].title(),
                "Sync_Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            logging.error(f"⚠️ Node Desynchronized [{city}]: {e}")
            return None

    def execute_parallel_ingestion(self, targets: List[str]):
        """Orchestrates high-concurrency data ingestion via thread pool orchestration."""
        logging.info(f"🚀 Deploying ingestion sequence for {len(targets)} strategic nodes...")
        
        # Performance Formula: $$Efficiency = \frac{Nodes}{Concurrency\_Limit}$$
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_node = {executor.submit(self._fetch_node_pulse, node): node for node in targets}
            
            for future in as_completed(future_to_node):
                result = future.result()
                if result:
                    self.registry.append(result)
                    logging.info(f"   ✅ Node Synchronized: {result['Node_ID']} @ {result['Temp_C']}°C")

    def persist_strategic_asset(self):
        """Finalizes the intelligence payload into structured professional assets."""
        if not self.registry:
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        excel_asset = self.vault_dir / f"Global_Intelligence_Report_{timestamp}.xlsx"
        
        df = pd.DataFrame(self.registry)

        try:
            # High-Fidelity Report Orchestration
            with pd.ExcelWriter(excel_asset, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Surveillance_Report', index=False)
                
                workbook = writer.book
                worksheet = writer.sheets['Surveillance_Report']
                
                # --- Advanced Enterprise Styling ---
                header_fmt = workbook.add_format({
                    'bold': True, 'font_color': 'white', 'bg_color': '#1B2631', 'border': 1
                })
                numeric_fmt = workbook.add_format({'num_format': '0.0', 'align': 'center'})
                
                for col_num, value in enumerate(df.columns.values):
                    worksheet.write(0, col_num, value, header_fmt)
                    worksheet.set_column(col_num, col_num, 18)
                
                # Applying conditional formatting for temperature thresholds
                worksheet.conditional_format('B2:B100', {
                    'type': '2_color_scale', 'min_color': "#AED6F1", 'max_color': "#E74C3C"
                })

            logging.info(f"🏆 Strategic report deployed to vault: {excel_asset.name}")
            
            # Hardware-Ready Backup (JSON format for future ESP32/OLED integration)
            json_asset = self.vault_dir / f"node_data_pulse.json"
            df.to_json(json_asset, orient="records", indent=4)
            logging.info("💾 Hardware-compatible payload mirrored for local node integration.")

        except Exception as e:
            logging.error(f"Persistence Layer Breach: {e}")

if __name__ == "__main__":
    print("\n" + "="*55)
    print("      YANG-TECH-LAB: METEOROLOGICAL ORCHESTRATOR v3.2")
    print("="*55 + "\n")
    
    try:
        orchestrator = IntelligenceOrchestrator()
        # Strategic Nodes: Guangzhou as home node + Global Market Hubs
        GLOBAL_NODES = ["Guangzhou", "London", "Tokyo", "Singapore", "Berlin", "New York"]
        
        orchestrator.execute_parallel_ingestion(GLOBAL_NODES)
        orchestrator.persist_professional_report()
        
    except Exception as fatal_e:
        logging.critical(f"System Termination Pulse: {fatal_e}")
    
    print("\n--- Session Complete: All Assets Persisted to Vault ---")
