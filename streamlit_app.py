# ============================================================
# LOANIQ — ENTERPRISE LOAN AMORTIZATION & ANALYTICS PLATFORM
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import io

# ============================================================
# FUNCTIONS (IMPORTANT: sh defined BEFORE use)
# ============================================================

def sh(title):
    st.markdown(f"## {title}")

def calculate_emi(principal, rate, months):
    r = rate / 100 / 12
    return principal * r * (1 + r)**months / ((1 + r)**months - 1)

def build_schedule(loan_amount, interest_rate, years, extra_payment=0):
    months = years * 12
    emi = calculate_emi(loan_amount, interest_rate, months)
    balance = loan_amount

    data = []
    for i in range(1, months + 1):
        interest = balance * interest_rate/100/12
        principal = emi - interest + extra_payment
        balance -= principal

        data.append({
            "Period": i,
            "Principal": principal,
            "Interest": interest,
            "Remaining Balance": max(balance, 0)
        })

        if balance <= 0:
            break

    return pd.DataFrame(data)

def chart_balance(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Period"], y=df["Remaining Balance"], fill="tozeroy"))
    return fig

def chart_pi(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Period"], y=df["Principal"], name="Principal"))
    fig.add_trace(go.Scatter(x=df["Period"], y=df["Interest"], name="Interest"))
    return fig

def chart_donut(p, i):
    fig = go.Figure(data=[go.Pie(labels=["Principal", "Interest"], values=[p,i], hole=.5)])
    return fig

# ============================================================
# MAIN
# ============================================================

def main():
    st.set_page_config(layout="wide")

    st.sidebar.title("Loan Settings")

    loan_amount = st.sidebar.number_input("Loan Amount", value=100000)
    interest_rate = st.sidebar.slider("Interest Rate", 1.0, 20.0, 8.5)
    years = st.sidebar.slider("Years", 1, 30, 10)
    extra = st.sidebar.number_input("Extra Payment", value=0)

    df = build_schedule(loan_amount, interest_rate, years, extra)

    total_interest = df["Interest"].sum()
    total_paid = loan_amount + total_interest

    # ============================================================
    # ✅ ENTERPRISE UI START
    # ============================================================

    sh("📊 Master Dashboard")

    # ✅ KPI ROW
