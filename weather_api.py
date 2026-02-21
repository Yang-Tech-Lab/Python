"""
WeatherSentinel Pro: High-Precision Meteorological Engine
---------------------------------------------------------
A modular, class-based utility designed to interface with global 
weather APIs and provide structured atmospheric intelligence.

Author: Yang-Lab (Yang Jiacheng)
Category: Automation / Intelligence Systems
Date: February 2026
"""

import requests
import logging
import sys
from typing import Dict, Optional, Final

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class WeatherSentinel:
    def __init__(self, api_key: str):
        self.api_key: Final[str] = api_key
        self.base_url: Final[str] = "http://api.openweathermap.org/data/2.5/weather"
        self.params: Dict[str, str] = {
            "units": "metric",
            "lang": "en"  # Standardized to English for international consistency
        }

    def fetch_weather_data(self, city: str) -> Optional[Dict]:
        """Initiates a network request to retrieve live atmospheric metrics."""
        query_params = {**self.params, "q": city, "appid": self.api_key}
        
        logging.info(f"Establishing connection for asset: {city}...")
        try:
            response = requests.get(self.base_url, params=query_params, timeout=12)
            response.raise_for_status() # Automatically handles HTTP errors (4xx, 5xx)
            return response.json()
        except requests.exceptions.HTTPError:
            logging.error(f"Target city '{city}' not found in global registry.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Network Protocol Failure: {e}")
        return None

    def display_metrics(self, data: Dict):
        """Parses and renders structured meteorological intelligence."""
        try:
            metrics = {
                "City": data['name'],
                "Temp": data['main']['temp'],
                "Humidity": data['main']['humidity'],
                "Condition": data['weather'][0]['description'],
                "Wind_Speed": data['wind']['speed']
            }

            print("\n" + "="*40)
            print(f"🌍 METEOROLOGICAL REPORT: [{metrics['City']}]")
            print(f"🌡️  Temperature: {metrics['Temp']}°C")
            print(f"☁️  Sky Condition: {metrics['Condition'].title()}")
            print(f"💧  Humidity Level: {metrics['Humidity']}%")
            print(f"🌬️  Wind Velocity: {metrics['Wind_Speed']} m/s")
            print("="*40 + "\n")
        except KeyError as e:
            logging.error(f"Data Schema Mismatch: Missing attribute {e}")

def main():
    # Deployment Parameters
    API_KEY = "103104f0c64435943e54807674a02704"
    sentinel = WeatherSentinel(API_KEY)

    print("--- Sentinel Protocol Initiated ---")
    while True:
        target = input("🌍 Enter city name (e.g., Beijing, London) or 'Q' to abort: ").strip()
        
        if target.lower() == 'q':
            logging.info("System shutdown sequence complete.")
            break
        
        if not target:
            continue

        raw_data = sentinel.fetch_weather_data(target)
        if raw_data:
            sentinel.display_metrics(raw_data)

if __name__ == "__main__":
    main()
