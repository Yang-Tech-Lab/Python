"""
Atmospheric Intelligence Node (DocuShield)
------------------------------------------
An industrial-grade meteorological engine with decoupled secret management 
for secure enterprise deployment.

Author: Yang-Tech-Lab (Yang Jiacheng)
Category: Systems Engineering / Cybersecurity
Date: March 2026
"""

import os
import logging
import requests
from typing import Dict, Optional, Final, Any
from dotenv import load_dotenv  # Standard for secret orchestration
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# 1. Initialize Secure Environment
# This loads variables from a local .env file into the system environment
load_dotenv()

console = Console()

class AtmosphericNode:
    def __init__(self):
        # Security: Fetching key from the OS environment instead of hardcoding
        self.__api_key: Final[str] = os.getenv("OPENWEATHER_API_KEY", "")
        self.endpoint: Final[str] = "https://api.openweathermap.org/data/2.5/weather"
        
        self._validate_security_layer()

    def _validate_security_layer(self):
        """Ensures the node is provisioned with valid credentials."""
        if not self.__api_key:
            logging.error("Security Breach: API Key missing from environment.")
            console.print("[bold red]❌ CRITICAL: OPENWEATHER_API_KEY not found in .env file![/bold red]")

    def fetch_metrics(self, city: str) -> Optional[Dict[str, Any]]:
        """Uplink to satellite to retrieve geospatial weather data."""
        params = {
            "q": city,
            "appid": self.__api_key,
            "units": "metric",
            "lang": "en"
        }
        
        try:
            response = requests.get(self.endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Handshake failure for {city}: {e}")
            return None

    def render_report(self, data: Dict[str, Any]):
        """Visualizes extracted telemetry in a high-fidelity table."""
        table = Table(title=f"Satellite Report: {data['name']}", header_style="bold cyan")
        table.add_column("Indicator", style="dim")
        table.add_column("Value")

        table.add_row("🌡️ Temp", f"{data['main']['temp']}°C")
        table.add_row("☁️ Sky", data['weather'][0]['description'].title())
        table.add_row("🌬️ Wind", f"{data['wind']['speed']} m/s")

        console.print(Panel(table, border_style="green", expand=False))

if __name__ == "__main__":
    node = AtmosphericNode()
    
    console.print(Panel.fit("🚀 [bold]Yang-Tech-Lab[/bold] | Secure Ingestion Active"))
    
    while True:
        target = console.input("\n[bold blue]Target City (or 'Q'): [/bold blue]").strip()
        if target.lower() == 'q': break
        if not target: continue

        with console.status("[bold green]Establishing secure link..."):
            raw_data = node.fetch_metrics(target)
            
        if raw_data:
            node.render_report(raw_data)
