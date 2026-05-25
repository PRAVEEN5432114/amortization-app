import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Enterprise Amortization Analytics",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #F8FAFC;
    }

    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        border-left: 6px solid #2563EB;
    }

    .summary-card {
        background: linear-gradient(135deg, #0F172A, #2563EB);
        color: white;
        padding: 20px;
        border-radius: 14px;
    }

    h1, h2, h3 {
        color: #0F172A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("Loan Configuration")

loan_amount = st.sidebar.number_input(
    "Loan Amount",
    min_value=1000,
    value=500000,
    step=10000
)

interest_rate = st.sidebar.slider(
    "Interest Rate (%)",
    1.0,
    25.0,
    8.5
)

loan_years = st.sidebar.slider(
    "Loan Tenure (Years)",
    1,
    40,
    15
)

extra_payment = st.sidebar.number_input(
    "Extra Monthly Payment",
    """
