"""
WealthOrchestrator Pro: Strategic Capital Accretion Interface
--------------------------------------------------------------
A high-fidelity financial simulation suite designed to model 
exponential growth trajectories via recursive compounding algorithms.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Fintech / Web Automation / Systems Engineering
Date: March 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from typing import List, Dict, Final, Tuple

# 1. Industrial UI Configuration & Custom Styling
st.set_page_config(
    page_title="WealthOrchestrator Pro | Yang-Tech-Lab", 
    page_icon="📈", 
    layout="wide"
)

# Professional CSS Injection for "Dark Tech" Aesthetic
st.markdown("""
    <style>
    .stMetric {
        background-color: #111111;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    [data-testid="stSidebar"] {
        background-color: #0e1117;
    }
    </style>
    """, unsafe_allow_html=True)

class WealthEngine:
    """The core mathematical node for recursive capital simulation."""
    
    @staticmethod
    def simulate_trajectory(
        periodic_injection: float, 
        years: int, 
        annual_yield: float
    ) -> pd.DataFrame:
        """
        Orchestrates the compounding sequence and generates a time-series dataset.
        
        Formula: $$FV = P \times \frac{(1 + r)^n - 1}{r}$$
        """
        months = years * 12
        monthly_rate = (annual_yield / 100) / 12
        
        balance = 0.0
        principal_accrued = 0.0
        data_points = []
        
        for m in range(1, months + 1):
            balance = (balance + periodic_injection) * (1 + monthly_rate)
            principal_accrued += periodic_injection
            
            data_points.append({
                "Month": m,
                "Year": round(m / 12, 2),
                "Portfolio_Valuation": round(balance, 2),
                "Principal_Baseline": round(principal_accrued, 2),
                "Net_Yield": round(balance - principal_accrued, 2)
            })
            
        return pd.DataFrame(data_points)

def render_interface():
    """Renders the executive dashboard and interactive controls."""
    st.title("🛰️ Strategic Capital Orchestration Interface")
    st.caption("Industrial-Grade Wealth Simulation Engine | Powered by Yang-Tech-Lab")

    # --- Sidebar: Parametric Controls ---
    st.sidebar.header("🕹️ Operational Parameters")
    
    with st.sidebar:
        injection = st.slider("Periodic Capital Injection ($/Mo)", 100, 20000, 1500, step=100)
        horizon = st.slider("Temporal Maturity Window (Years)", 5, 50, 25)
        yield_rate = st.slider("Targeted Annual Yield (%)", 1, 30, 12)
        
        st.divider()
        st.info("💡 Tip: 12% is a historical benchmark for diversified equity indices.")

    # --- Engine Execution ---
    engine = WealthEngine()
    df = engine.simulate_trajectory(injection, horizon, yield_rate)
    
    # KPIs Extraction
    final_valuation = df.iloc[-1]["Portfolio_Valuation"]
    total_principal = df.iloc[-1]["Principal_Baseline"]
    net_gain = df.iloc[-1]["Net_Yield"]

    # --- Section 1: Strategic Intelligence Metrics ---
    st.subheader("📊 Executive Summary")
    m_col1, m_col2, m_col3 = st.columns(3)
    
    m_col1.metric("Total Principal Committed", f"${total_principal:,.0f}")
    m_col2.metric("Projected Portfolio Value", f"${final_valuation:,.0f}")
    m_col3.metric("Net Wealth Accretion", f"${net_gain:,.0f}", 
                delta=f"{((net_gain/total_principal)*100):.1f}% ROI")

    # --- Section 2: Visual Intelligence (Dynamic Plotly) ---
    st.subheader("📈 Future Value Trajectory")
    
    fig = go.Figure()
    
    # Portfolio Growth Area
    fig.add_trace(go.Scatter(
        x=df['Year'], y=df['Portfolio_Valuation'],
        mode='lines',
        name='Compounded Equity',
        line=dict(width=3, color='#3498db'),
        fill='tozeroy',
        fillcolor='rgba(52, 152, 219, 0.1)'
    ))
    
    # Principal Baseline
    fig.add_trace(go.Scatter(
        x=df['Year'], y=df['Principal_Baseline'],
        mode='lines',
        name='Principal Baseline',
        line=dict(width=2, color='#e74c3c', dash='dot')
    ))

    fig.update_layout(
        template="plotly_dark",
        hovermode="x unified",
        margin=dict(l=0, r=0, t=20, b=0),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis_title="Timeline (Years)",
        yaxis_title="Valuation (USD)",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # --- Section 3: Technical Metadata ---
    st.divider()
    exp1, exp2 = st.columns(2)
    
    with exp1:
        with st.expander("📝 Mathematical Foundations"):
            st.write("The simulation leverages the standard annuity formula:")
            st.latex(r"FV = P \times \frac{(1 + r)^n - 1}{r}")
            st.caption("P=Injection, r=Monthly Rate, n=Months.")

    with exp2:
        with st.expander("📁 Raw Intelligence Payload"):
            st.dataframe(df.tail(10), use_container_width=True)

    st.caption("System Architect: Yang Jiacheng | High-Fidelity Automation & IoT Logic.")

if __name__ == "__main__":
    render_interface()
