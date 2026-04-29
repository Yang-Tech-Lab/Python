"""
WeatherSentinel Pro: Advanced Geospatial Intelligence Dashboard
---------------------------------------------------------------
An enterprise-grade Web-UI designed for real-time atmospheric 
surveillance and geospatial data orchestration.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Full-Stack Systems / IoT Automation
Date: April 24, 2026
"""

import os
import logging
import requests
import pandas as pd
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, Optional, Final

# 1. Initialize Secure Environment & Infrastructure
load_dotenv() # Ingests secrets from .env file

st.set_page_config(
    page_title="WeatherSentinel Pro | Yang-Tech-Lab",
    page_icon="🛰️",
    layout="wide"
)

# Professional CSS: Industrial Dark Theme
st.markdown("""
    <style>
    .stMetric {
        background-color: #0e1117;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #2563eb;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

class AtmosphericEngine:
    def __init__(self):
        # Security Protocol: Hardcoded key removed. 
        # Source: Environment variables or Streamlit Secrets
        self.__api_key: Final[str] = os.getenv("OPENWEATHER_API_KEY", "")
        self.base_url: Final[str] = "https://api.openweathermap.org/data/2.5/weather"

    def execute_satellite_scan(self, city: str) -> Optional[Dict]:
        """Orchestrates a satellite handshake for atmospheric metrics."""
        if not self.__api_key:
            st.error("❌ CRITICAL: API Key not detected in secure environment.")
            return None

        params = {
            "q": city,
            "appid": self.__api_key,
            "units": "metric",
            "lang": "en"
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=15)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Uplink Failure: {e}")
            return None

def main():
    # --- Header Orchestration ---
    st.title("🛰️ Atmospheric Intelligence Interface")
    st.caption("Industrial-Grade Weather Surveillance Node | Version 2.0.26")
    
    # --- Sidebar: Parametric Control ---
    st.sidebar.header("🕹️ Tactical Controls")
    target_node = st.sidebar.text_input("Geospatial Target (City Name):", "Guangzhou")
    unit_system = st.sidebar.selectbox("Unit System:", ["Metric (°C)", "Imperial (°F)"])
    scan_triggered = st.sidebar.button("Execute Intelligence Scan")

    engine = AtmosphericEngine()

    if scan_triggered:
        with st.status("Establishing satellite uplink...", expanded=True) as status:
            data = engine.execute_satellite_scan(target_node)
            if data:
                status.update(label="Scan Sequence Complete. Rendering Intelligence.", state="complete")
                
                # --- Phase 1: Geospatial Positioning ---
                lat, lon = data['coord']['lat'], data['coord']['lon']
                col_info, col_map = st.columns([1, 1])

                with col_info:
                    st.header(f"📍 {data['name']}, {data['sys']['country']}")
                    st.markdown(f"**Coordinates:** `{lat} N, {lon} E`")
                    st.markdown(f"**Observation Sync:** `{datetime.now().strftime('%H:%M:%S')}`")
                    
                    # Condition Display
                    icon = data['weather'][0]['icon']
                    desc = data['weather'][0]['description'].upper()
                    st.image(f"https://openweathermap.org/img/wn/{icon}@4x.png", width=150)
                    st.info(f"Condition: **{desc}**")

                with col_map:
                    # Rendering high-fidelity map asset
                    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
                    st.map(map_data, zoom=10, use_container_width=True)

                # --- Phase 2: High-Fidelity Metrics ---
                st.divider()
                m1, m2, m3, m4 = st.columns(4)
                
                temp = data['main']['temp']
                m1.metric("Temperature", f"{temp}°C", f"Feels {data['main']['feels_like']}°C")
                m2.metric("Humidity", f"{data['main']['humidity']}%")
                m3.metric("Wind Velocity", f"{data['wind']['speed']} m/s")
                m4.metric("Barometric Pressure", f"{data['main']['pressure']} hPa")

                # --- Phase 3: Raw Payload Inspection ---
                st.divider()
                with st.expander("📁 Inspect Raw Ingestion Payload (JSON)"):
                    st.json(data)
            else:
                st.error("❌ Handshake failure. Target node unreachable or invalid.")
    else:
        st.info("👈 System standby. Input geospatial target to initiate surveillance.")

    # --- Footer Branding ---
    st.sidebar.divider()
    st.sidebar.caption("System Architect: Yang Jiacheng")
    st.sidebar.caption("Branch: Yang-Tech-Lab / Full-Stack")

if __name__ == "__main__":
    main()
