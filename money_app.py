"""
Wealth-Compound Intelligence Engine
-----------------------------------
A professional-grade financial simulation utility designed to model 
long-term asset accretion via automated compounding algorithms.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Fintech / Web Automation
Date: February 2026
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Page Configuration (Enterprise Branding)
st.set_page_config(page_title="Wealth-Lab Pro", page_icon="📈", layout="wide")

st.title('🚀 Wealth-Compound Intelligence Engine')
st.markdown("""
This interactive simulation models the trajectory of **capital accretion** over time. 
Leveraging the power of exponential growth, it projects the future value of systemic investments.
""")

# 2. Deployment Parameters (Sidebar)
st.sidebar.header('⚙️ Configuration Metrics')

# Use standard financial terms: Monthly Contribution, Horizon, and Annual Yield
monthly_contribution = st.sidebar.slider('Monthly Contribution ($)', 100, 10000, 1000)
investment_horizon = st.sidebar.slider('Investment Horizon (Years)', 1, 40, 20)
# Default set to 15% to reflect historical Nasdaq-100 (QQQ) benchmarks
target_annual_yield = st.sidebar.slider('Target Annual Yield (%)', 1, 30, 15)

# 3. Core Simulation Logic
# Formula: Future Value of an Annuity
# FV = P * [((1 + r)^n - 1) / r]
months = investment_horizon * 12
monthly_rate = (target_annual_yield / 100) / 12

future_value = 0
total_principal = 0
equity_trajectory = []

for _ in range(months):
    future_value = (future_value + monthly_contribution) * (1 + monthly_rate)
    total_principal += monthly_contribution
    equity_trajectory.append(future_value)

net_capital_gain = future_value - total_principal

# 4. Key Performance Indicators (KPIs)
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Invested Principal", f"${total_principal:,.0f}")
with col2:
    st.metric("Projected Equity", f"${future_value:,.0f}")
with col3:
    st.metric("Net Capital Gain", f"${net_capital_gain:,.0f}", delta=f"{((net_capital_gain/total_principal)*100):.1f}%")

# 5. Visual Intelligence Layer
st.subheader('📈 Asset Accretion Trajectory')

# Professional Plotting with Matplotlib
fig, ax = plt.subplots(figsize=(12, 6))
plt.style.use('dark_background') # Aesthetic matching your developer profile

ax.fill_between(range(months), equity_trajectory, color='#3498db', alpha=0.3, label='Compounded Growth')
ax.plot(equity_trajectory, color='#3498db', linewidth=3, label='Total Portfolio Value')
ax.plot([0, months], [0, total_principal], color='#e74c3c', linestyle='--', label='Principal Baseline')

ax.set_title("Long-Term Wealth Projection", fontsize=16, color='white', pad=20)
ax.set_xlabel("Months in Market", fontsize=10, color='#bdc3c7')
ax.set_ylabel("Portfolio Valuation ($)", fontsize=10, color='#bdc3c7')
ax.legend(facecolor='#2c3e50')
ax.grid(True, alpha=0.1)

# Render plot to Streamlit
st.pyplot(fig)

# 6. Technical Footer & Documentation
st.divider()
with st.expander("📝 View Mathematical Foundation"):
    st.write("The engine utilizes the **Future Value of an Ordinary Annuity** formula:")
    st.latex(r"FV = P \times \frac{(1 + r)^n - 1}{r}")
    st.caption("Where P = Periodic Payment, r = Periodic Interest Rate, n = Total Number of Periods.")

st.caption("Engineered by Yang Jiacheng | Powering remote financial freedom through code.")
