"""
Meteorological Intelligence Orchestrator (Enterprise)
----------------------------------------------------
An advanced asynchronous-ready data acquisition engine with enhanced 
security, error recovery, and professional report formatting.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Automation
Date: February 2026
"""

import os
import time
import logging
import pandas as pd
import requests
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Final, TypedDict

# 1. Advanced Logging Configuration (Log to both console and file)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("system_audit.log"),
        logging.StreamHandler()
    ]
)

# 2. Define Data Schema for strict consistency
class WeatherSchema(TypedDict):
    Node_ID: str
    Temp_C: float
    Condition: str
    Humidity: int
    Metadata_Sync: str

class WeatherIntelligenceEngine:
    def __init__(self, api_key: Optional[str] = None):
        # Security First: Priority given to Environment Variables
        self.__api_key: Final[str] = api_key or os.getenv("OPENWEATHER_API_KEY", "")
        self.base_url: Final[str] = "https://api.openweathermap.org/data/2.5/weather"
        self.registry: List[WeatherSchema] = []
        self.output_path: Final[Path] = Path("Global_Market_Weather_Intelligence.xlsx")

        if not self.__api_key:
            logging.critical("Security Breach: Missing API Key in Environment Variables.")
            raise ValueError("API Key is required for orchestration.")

    def _fetch_with_retry(self, city: str, retries: int = 3) -> Optional[Dict]:
        """Handshake with API using exponential backoff logic."""
        params = {"q": city, "appid": self.__api_key, "units": "metric", "lang": "en"}
        
        for attempt in range(retries):
            try:
                response = requests.get(self.base_url, params=params, timeout=15)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                wait_time = (attempt + 1) * 2
                logging.warning(f"Connection unstable for {city}. Retrying in {wait_time}s... Error: {e}")
                time.sleep(wait_time)
        return None

    def execute_acquisition_pipeline(self, nodes: List[str]):
        """Orchestrates data ingestion for all targeted geospatial nodes."""
        logging.info(f"🚀 Initializing Acquisition Pipeline for {len(nodes)} strategic nodes.")
        
        for city in nodes:
            raw_payload = self._fetch_with_retry(city)
            if raw_payload:
                # Data Transformation Layer
                entity: WeatherSchema = {
                    "Node_ID": city.upper(),
                    "Temp_C": raw_payload['main']['temp'],
                    "Condition": raw_payload['weather'][0]['description'].title(),
                    "Humidity": raw_payload['main']['humidity'],
                    "Metadata_Sync": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                self.registry.append(entity)
                logging.info(f"   ✅ Node Synchronized: {city} | Metric: {entity['Temp_C']}°C")
            
            # Intelligent Throttling
            time.sleep(1.0)

    def persist_professional_report(self):
        """Persists data with professional Excel formatting for client delivery."""
        if not self.registry:
            logging.error("Persistence Aborted: Registry is empty.")
            return

        logging.info(f"💾 Generating high-fidelity report at: {self.output_path}")
        df = pd.DataFrame(self.registry)

        # Use XlsxWriter for "Premium" report formatting
        try:
            with pd.ExcelWriter(self.output_path, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Intelligence_Report', index=False)
                
                # Accessing the underlying workbook/worksheet for styling
                workbook = writer.book
                worksheet = writer.sheets['Intelligence_Report']
                
                # Define Professional Styles
                header_format = workbook.add_format({
                    'bold': True, 'font_color': 'white', 'bg_color': '#2C3E50', 'border': 1
                })

                # Apply Header Format & Auto-adjust column width
                for col_num, value in enumerate(df.columns.values):
                    worksheet.write(0, col_num, value, header_format)
                    worksheet.set_column(col_num, col_num, len(value) + 10)

            logging.info("🏆 Professional Report Deployed Successfully.")
        except Exception as e:
            logging.error(f"Persistence Layer Failure: {e}")

if __name__ == "__main__":
    # Standard Operating Procedure (SOP)
    # Recommended: Set env var via 'export OPENWEATHER_API_KEY=your_key'
    print("--- Sentinel Protocol Offline: System Initializing ---")
    
    try:
        # Injects API Key from environment (Best Practice)
        engine = WeatherIntelligenceEngine()
        
        TARGET_NODES = ["London", "New York", "Tokyo", "Singapore", "Guangzhou", "Berlin"]
        engine.execute_acquisition_pipeline(TARGET_NODES)
        engine.persist_professional_report()
        
    except Exception as e:
        logging.critical(f"System Crash: {e}")
        
    print("-" * 55)
