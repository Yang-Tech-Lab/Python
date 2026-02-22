"""
WeatherSentinel Pro: Automated Meteorological Intelligence Dashboard
-------------------------------------------------------------------
A high-performance Web-UI designed to interface with global weather grids 
and render real-time atmospheric metrics.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Full-Stack Web Automation
Date: February 2026
"""

import streamlit as st
import requests
import logging
from datetime import datetime
from typing import Dict, Optional, Final

# 1. Industrial Configuration & Branding
st.set_page_config(
    page_title="WeatherSentinel Pro", 
    page_icon="📡", 
    layout="wide"
)

# Professional CSS to refine UI aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

class WeatherEngine:
    """Handles all geospatial data acquisition and API interactions."""
    def __init__(self, api_key: str):
        self.api_key: Final[str] = api_key
        self.base_url: Final[str] = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_meteorological_data(self, city: str) -> Optional[Dict]:
        """Initiates a satellite handshake to retrieve real-time data."""
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "en" # Standardized for international deliverables
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=12)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            logging.error(f"Atmospheric Data Ingestion Failed: {e}")
            return None

def render_dashboard():
    """Orchestrates the UI rendering and data visualization."""
    st.title("🛰️ Atmospheric Intelligence Interface")
    st.caption("Global Real-Time Weather Surveillance | Powered by Yang-Tech-Lab Engine")

    # --- Sidebar: Operational Control ---
    st.sidebar.header("🕹️ Operational Controls")
    target_city = st.sidebar.text_input("Geospatial Target (City):", "Guangzhou")
    execute_scan = st.sidebar.button("Execute Satellite Scan")

    # API Key Management (In production, use st.secrets)
    API_KEY = "103104f0c64435943e54807674a02704"
    engine = WeatherEngine(API_KEY)

    if execute_scan:
        with st.spinner('Initiating satellite uplink...'):
            data = engine.fetch_meteorological_data(target_city)
            
            if data:
                # 1. Coordinate & Header Section
                lat, lon = data['coord']['lat'], data['coord']['lon']
                st.subheader(f"📍 Target Identified: {data['name']} [{lat}, {lon}]")
                
                # 2. Icon & Summary
                icon_code = data['weather'][0]['icon']
                condition = data['weather'][0]['description'].upper()
                col_icon, col_text = st.columns([1, 4])
                with col_icon:
                    st.image(f"https://openweathermap.org/img/wn/{icon_code}@4x.png")
                with col_text:
                    st.markdown(f"### Current Status: **{condition}**")
                    st.info(f"Local time observation synchronized from global grid.")

                # 3. High-Fidelity Metrics
                st.divider()
                m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                
                # Temperature Data
                temp = data['main']['temp']
                feels = data['main']['feels_like']
                m_col1.metric("Temperature", f"{temp}°C", f"Feels like {feels}°C")
                
                # Humidity Analytics
                humidity = data['main']['humidity']
                m_col2.metric("Humidity", f"{humidity}%")
                
                # Velocity Vectors
                wind_speed = data['wind']['speed']
                m_col3.metric("Wind Velocity", f"{wind_speed} m/s")
                
                # Atmospheric Pressure
                pressure = data['main']['pressure']
                m_col4.metric("Barometric Pressure", f"{pressure} hPa")

                # 4. Intelligence Payload (Raw Data)
                st.divider()
                with st.expander("📁 Inspect Raw Data Payload (JSON)"):
                    st.json(data)
            else:
                st.error("❌ Target identification failed. Please verify the city name or network status.")
    else:
        st.write("---")
        st.warning("👈 Awaiting geospatial target input to initiate scan sequence.")

if __name__ == "__main__":
    render_dashboard()
