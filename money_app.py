"""
WealthOrchestrator Pro: v6.0 Autonomous Fiscal Engine
-----------------------------------------------------
An industrial-grade capital orchestration suite designed for 
deterministic growth modeling, recursive compounding analysis, 
and high-fidelity visual telemetry.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Fintech Systems / Full-Stack Automation
Date: April 16, 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
from typing import Final, Dict, List, Optional

# 1. Industrial Infrastructure & UI Configuration
st.set_page_config(
    page_title="WealthOrchestrator v6.0 | Yang-Tech-Lab",
    page_icon="🛰️",
    layout="wide"
)

# Custom CSS for "Industrial-Grade" aesthetic
st.markdown("""
    <style>
    .main { background-color: #0A0A0A; }
    .stMetric {
        background-color: #161B22;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #30363D;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .stSlider > label { font-weight: bold; color: #58A6FF; }
    </style>
    """, unsafe_allow_html=True)

class FiscalOrchestrator:
    """The core intelligence node for non-linear capital trajectory modeling."""
    
    @staticmethod
    def execute_simulation(
        monthly_injection: float, 
        horizon_years: int, 
        annual_yield: float,
        inflation_rate: float = 3.0
    ) -> pd.DataFrame:
        """
        Orchestrates the compounding sequence with recursive inflation-adjustment logic.
        
        Standard Annuity Formula:
        $$FV = P \times \frac{(1 + r)^n - 1}{r}$$
        """
        months: Final[int] = horizon_years * 12
        monthly_yield_rate = (annual_yield / 100) / 12
        monthly_inflation_rate = (inflation_rate / 100) / 12
        
        nominal_balance = 0.0
        real_balance = 0.0  # Inflation-adjusted value
        cumulative_principal = 0.0
        telemetry_logs = []
        
        for m in range(1, months + 1):
            nominal_balance = (nominal_balance + monthly_injection) * (1 + monthly_yield_rate)
            real_balance = (real_balance + monthly_injection) * (1 + monthly_yield_rate - monthly_inflation_rate)
            cumulative_principal += monthly_injection
            
            if m % 12 == 0 or m == months:
                telemetry_logs.append({
                    "Year": m // 12,
                    "Nominal_Valuation": round(nominal_balance, 2),
                    "Real_Purchasing_Power": round(real_balance, 2),
                    "Principal_Baseline": round(cumulative_principal, 2),
                    "Accrued_Alpha": round(nominal_balance - cumulative_principal, 2)
                })
                
        return pd.DataFrame(telemetry_logs)

def render_dashboard():
    """Synthesizes the executive dashboard and control interface."""
    st.title("🛰️ Strategic Wealth Orchestration Suite")
    st.caption(f"System Architect: Yang Jiacheng (Yang-Tech-Lab) | Node Status: Online | {datetime.now().strftime('%Y-%m-%d')}")

    # --- Sidebar: Parametric Input Layer ---
    st.sidebar.header("🕹️ Tactical Controls")
    with st.sidebar:
        st.subheader("Capital Ingestion")
        p_injection = st.number_input("Monthly Injection (USD)", 0, 100000, 2000, step=500)
        p_horizon = st.slider("Horizon Window (Years)", 1, 50, 20)
        
        st.subheader("Yield Telemetry")
        p_yield = st.slider("Targeted Annual Yield (%)", 0.0, 40.0, 10.0, step=0.5)
        p_inflation = st.checkbox("Apply Inflation Adjustment (3.0% std)", value=True)
        
        st.divider()
        st.caption("2026 Standard: S&P 500 Historical Yield ~10.5%")

    # --- Engine Execution ---
    engine = FiscalOrchestrator()
    inflation_val = 3.0 if p_inflation else 0.0
    df = engine.execute_simulation(p_injection, p_horizon, p_yield, inflation_val)
    
    # KPIs Extraction
    final_node = df.iloc[-1]
    
    # --- Phase 1: High-Fidelity Metrics ---
    st.subheader("📊 Executive Intelligence Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Principal Committed", f"${final_node['Principal_Baseline']:,.0f}")
    col2.metric("Nominal Portfolio", f"${final_node['Nominal_Valuation']:,.0f}")
    col3.metric("Purchasing Power (Real)", f"${final_node['Real_Purchasing_Power']:,.0f}")
    
    roi_pct = (final_node['Accrued_Alpha'] / final_node['Principal_Baseline']) * 100
    col4.metric("Net Alpha Accretion", f"${final_node['Accrued_Alpha']:,.0f}", delta=f"{roi_pct:.1f}% Total ROI")

    # --- Phase 2: Visual Intelligence (Plotly Orchestration) ---
    st.subheader("📈 Future Value Trajectory & Volatility Simulation")
    
    fig = go.Figure()
    
    # Nominal Growth Area
    fig.add_trace(go.Scatter(
        x=df['Year'], y=df['Nominal_Valuation'],
        mode='lines+markers', name='Nominal Valuation',
        line=dict(color='#58A6FF', width=4),
        fill='tozeroy', fillcolor='rgba(88, 166, 255, 0.1)'
    ))
    
    # Real Purchasing Power
    if p_inflation:
        fig.add_trace(go.Scatter(
            x=df['Year'], y=df['Real_Purchasing_Power'],
            mode='lines', name='Real Value (Inflation-Adj)',
            line=dict(color='#238636', width=2, dash='dash')
        ))
    
    # Principal Baseline
    fig.add_trace(go.Scatter(
        x=df['Year'], y=df['Principal_Baseline'],
        mode='lines', name='Principal Committed',
        line=dict(color='#F85149', width=2, dash='dot')
    ))

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis=dict(title="Operational Horizon (Years)", gridcolor='#30363D'),
        yaxis=dict(title="Valuation (USD)", gridcolor='#30363D')
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # --- Phase 3: Technical Appendix ---
    st.divider()
    c1, c2 = st.columns([2, 1])
    with c1:
        with st.expander("📁 Inspect Raw Intelligence Payload (JSON/CSV)"):
            st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
    with c2:
        with st.expander("🛠️ System Architecture"):
            st.info("Deterministic Logic Gate: Compound Interest.")
            st.latex(r"Accretion_{Rate} = \sum_{m=1}^{n} (I \times (1+r)^m)")
            st.caption("Engine: Yang-Tech-Lab v6.0")

if __name__ == "__main__":
    render_dashboard()
