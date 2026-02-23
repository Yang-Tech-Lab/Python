"""
Meteorological Intelligence Orchestrator
----------------------------------------
A robust, asynchronous-ready data acquisition engine designed to interface 
with global weather APIs and persist structured analytics to Excel.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Data Engineering / Business Automation
Date: February 2026
"""

import requests
import pandas as pd
import logging
from datetime import datetime
import time
from pathlib import Path
from typing import List, Dict, Optional, Final

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class WeatherIntelligenceEngine:
    def __init__(self, api_key: str):
        self.api_key: Final[str] = api_key
        self.base_url: Final[str] = "http://api.openweathermap.org/data/2.5/weather"
        self.dataset: List[Dict] = []
        self.persistence_path: Final[Path] = Path("Global_Weather_Analytics_Report.xlsx")

    def fetch_geospatial_weather(self, city: str) -> Optional[Dict]:
        """Initiates a network handshake to retrieve atmospheric metrics for a target city."""
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "en" # Standardized to English for international deliverables
        }
        
        logging.info(f"Establishing connection for target: {city}...")
        try:
            response = requests.get(self.base_url, params=params, timeout=12)
            response.raise_for_status()
            data = response.json()
            
            # Data Transformation Layer
            return {
                "City": city,
                "Temperature_Celsius": data['main']['temp'],
                "Atmospheric_Condition": data['weather'][0]['description'].title(),
                "Humidity_Percentage": data['main']['humidity'],
                "Synchronized_At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except requests.exceptions.RequestException as e:
            logging.error(f"Network Protocol Failure for {city}: {e}")
            return None

    def execute_batch_acquisition(self, target_cities: List[str]):
        """Orchestrates the acquisition sequence with adaptive throttling."""
        logging.info(f"🚀 Initializing Batch Acquisition Sequence for {len(target_cities)} nodes...")
        
        for city in target_cities:
            metrics = self.fetch_geospatial_weather(city)
            if metrics:
                self.dataset.append(metrics)
                logging.info(f"   ✅ Synchronized: {metrics['Temperature_Celsius']}°C | {metrics['Atmospheric_Condition']}")
            
            # Throttling logic to maintain API stability (Rate Limiting)
            time.sleep(0.8)

    def persist_to_excel(self):
        """Persists the acquired dataset to a structured Excel binary."""
        if not self.dataset:
            logging.warning("Deployment aborted: No valid data identified in the registry.")
            return

        logging.info(f"💾 Initializing persistence layer: Writing to {self.persistence_path}...")
        try:
            df = pd.DataFrame(self.dataset)
            df.to_excel(self.persistence_path, index=False)
            logging.info("🏆 Mission Accomplished. Strategic analytics report is ready for deployment.")
        except Exception as e:
            logging.error(f"Persistence Layer Failure: {e}")

if __name__ == "__main__":
    # Deployment Parameters
    SECRET_KEY = "103104f0c64435943e54807674a02704"
    TARGET_NODES = ["Beijing", "Shanghai", "Tokyo", "New York", "London", "Paris", "Berlin"]

    # Engine Execution
    print("--- Sentinel Protocol Offline: System Initializing ---")
    engine = WeatherIntelligenceEngine(api_key=SECRET_KEY)
    engine.execute_batch_acquisition(TARGET_NODES)
    engine.persist_to_excel()
    print("-" * 50)
