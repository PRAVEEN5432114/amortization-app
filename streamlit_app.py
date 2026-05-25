# ============================================================
# ENTERPRISE LOAN AMORTIZATION & FINANCIAL ANALYTICS PLATFORM
# Production-Ready | EPM-Grade | Streamlit + Plotly
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="LoanIQ | Enterprise Amortization Analytics",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS — ENTERPRISE FINTECH STYLING
# ============================================================

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    /* ---- GLOBAL ---- */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main { background-color: #F8FAFC; }

    /* ---- HEADER BANNER ---- */
    .app-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A5F 50%, #0F172A 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        border: 1px solid #1E40AF;
        position: relative;
        overflow: hidden;
    }
    .app-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(37,99,235,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .app-header h1 {
        color: #FFFFFF;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .app-header p {
        color: #94A3B8;
        margin: 0.4rem 0 0 0;
        font-size: 0.95rem;
    }
    .header-badge {
        display: inline-block;
        background: rgba(37,99,235,0.3);
        border: 1px solid #2563EB;
        color: #93C5FD;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }

    /* ---- KPI CARDS ---- */
    .kpi-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }
    .kpi-label {
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: #64748B;
        margin-bottom: 0.4rem;
    }
    .kpi-value {
        font-size: 1.7rem;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.1;
        font-family: 'JetBrains Mono', monospace;
    }
    .kpi-sub {
        font-size: 0.78rem;
        color: #94A3B8;
        margin-top: 0.3rem;
    }
    .kpi-delta-pos { color: #10B981; font-weight: 600; font-size: 0.8rem; }
    .kpi-delta-neg { color: #EF4444; font-weight: 600; font-size: 0.8rem; }
    .kpi-icon {
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    .kpi-card.accent-blue { border-left: 4px solid #2563EB; }
    .kpi-card.accent-green { border-left: 4px solid #10B981; }
    .kpi-card.accent-amber { border-left: 4px solid #F59E0B; }
    .kpi-card.accent-red   { border-left: 4px solid #EF4444; }
    .kpi-card.accent-cyan  { border-left: 4px solid #06B6D4; }
    .kpi-card.accent-purple{ border-left: 4px solid #8B5CF6; }

    /* ---- SECTION TITLES ---- */
    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin: 1.8rem 0 0.6rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #E2E8F0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* ---- INSIGHT CARDS ---- */
    .insight-card {
        background: linear-gradient(135deg, #EFF6FF, #F0F9FF);
        border: 1px solid #BFDBFE;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .insight-card.warn {
        background: linear-gradient(135deg, #FFFBEB, #FFF7ED);
        border-color: #FDE68A;
    }
    .insight-card.success {
        background: linear-gradient(135deg, #ECFDF5, #F0FDF4);
        border-color: #A7F3D0;
    }
    .insight-card.danger {
        background: linear-gradient(135deg, #FEF2F2, #FFF1F2);
        border-color: #FECACA;
    }

    /* ---- SIDEBAR ---- */
    [data-testid="stSidebar"] {
        background: #0F172A;
    }
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .st-emotion-cache-16idsys p {
        color: #CBD5E1 !important;
    }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
    }

    /* ---- TABLE STYLING ---- */
    .styled-table {
        font-size: 0.85rem;
    }

    /* ---- METRIC OVERRIDE ---- */
    div[data-testid="metric-container"] {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 1px 6px rgba(0,0,0,0.04);
    }

    /* ---- TABS ---- */
    .stTabs [data-baseweb="tab-list"] {
        background: #F1F5F9;
        border-radius: 10px;
        padding: 4px;
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        font-weight: 500;
        font-size: 0.9rem;
    }

    /* ---- RISK BADGE ---- */
    .risk-low    { background:#D1FAE5; color:#065F46; padding:4px 12px; border-radius:20px; font-size:0.8rem; font-weight:600; }
    .risk-medium { background:#FEF3C7; color:#92400E; padding:4px 12px; border-radius:20px; font-size:0.8rem; font-weight:600; }
    .risk-high   { background:#FEE2E2; color:#991B1B; padding:4px 12px; border-radius:20px; font-size:0.8rem; font-weight:600; }

    /* ---- DOWNLOAD BUTTON ---- */
    .stDownloadButton button {
        background: #2563EB;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
        transition: background 0.2s;
    }
    .stDownloadButton button:hover { background: #1D4ED8; }

    /* ---- FOOTER ---- */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #94A3B8;
        font-size: 0.8rem;
        border-top: 1px solid #E2E8F0;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# UTILITY: CURRENCY FORMATTER
# ============================================================

CURRENCY_SYMBOLS = {
    "INR (₹)": "₹",
    "USD ($)": "$",
    "EUR (€)": "€",
    "GBP (£)": "£",
    "AED (د.إ)": "د.إ",
    "JPY (¥)": "¥",
}

def fmt(value: float, symbol: str, decimals: int = 2) -> str:
    """Format a number as currency string."""
    if abs(value) >= 1_00_00_000:   # crores (Indian)
        return f"{symbol}{value/1_00_00_000:,.2f} Cr"
    elif abs(value) >= 1_00_000:     # lakhs
        return f"{symbol}{value/1_00_000:,.2f} L"
    elif abs(value) >= 1_000:
        return f"{symbol}{value:,.{decimals}f}"
    else:
        return f"{symbol}{value:.{decimals}f}"

def fmt_plain(value: float, symbol: str) -> str:
    """Plain currency format without abbreviation."""
    return f"{symbol}{value:,.2f}"

# ============================================================
# CORE: EMI CALCULATION
# ============================================================

def calculate_emi(principal: float, annual_rate: float, months: int) -> float:
    """Standard EMI formula."""
    if annual_rate == 0:
        return principal / months
    r = annual_rate / 100 / 12
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)

# ============================================================
# CORE: AMORTIZATION SCHEDULE
# ============================================================

def build_schedule(
    loan_amount: float,
    annual_rate: float,
    loan_years: int,
    extra_payment: float = 0,
    frequency: str = "Monthly"
) -> pd.DataFrame:
    """
    Build a full amortization schedule supporting Monthly / Quarterly / Annual.
    Returns a DataFrame with period-level breakdowns.
    """
    freq_map = {"Monthly": 12, "Quarterly": 4, "Annual": 1}
    periods_per_year = freq_map[frequency]
    total_periods = loan_years * periods_per_year
    period_rate = annual_rate / 100 / periods_per_year

    if period_rate == 0:
        base_payment = loan_amount / total_periods
    else:
        base_payment = (
            loan_amount
            * period_rate
            * (1 + period_rate) ** total_periods
            / ((1 + period_rate) ** total_periods - 1)
        )

    extra_per_period = extra_payment * (12 / periods_per_year)
    payment = base_payment + extra_per_period

    schedule = []
    balance = loan_amount
    cumulative_interest = 0
    cumulative_principal = 0

    for period in range(1, total_periods + 1):
        interest_charge = balance * period_rate
        principal_charge = payment - interest_charge

        if principal_charge > balance:
            principal_charge = balance
            payment = principal_charge + interest_charge

        balance -= principal_charge
        cumulative_interest += interest_charge
        cumulative_principal += principal_charge

        schedule.append({
            "Period": period,
            "Payment": round(payment, 2),
            "Principal": round(principal_charge, 2),
            "Interest": round(interest_charge, 2),
            "Cumulative Interest": round(cumulative_interest, 2),
            "Cumulative Principal": round(cumulative_principal, 2),
            "Remaining Balance": round(max(balance, 0), 2),
        })

        if balance <= 0:
            break

    return pd.DataFrame(schedule)


def build_no_extra_schedule(
    loan_amount: float,
    annual_rate: float,
    loan_years: int,
    frequency: str = "Monthly"
) -> pd.DataFrame:
    """Schedule without extra payments (baseline for comparison)."""
    return build_schedule(loan_amount, annual_rate, loan_years, 0, frequency)

# ============================================================
# CORE: SCENARIO COMPARISON
# ============================================================

def multi_scenario(loan_amount, base_rate, loan_years, currency):
    """Generate multiple rate/tenure scenarios for comparison."""
    scenarios = []
    rates = [base_rate - 2, base_rate - 1, base_rate, base_rate + 1, base_rate + 2]
    tenures = [loan_years - 5, loan_years, loan_years + 5]

    for rate in rates:
        if rate <= 0:
            continue
        for tenure in tenures:
            if tenure <= 0:
                continue
            months = tenure * 12
            emi = calculate_emi(loan_amount, rate, months)
            total = emi * months
            interest = total - loan_amount
            scenarios.append({
                "Rate (%)": rate,
                "Tenure (Yrs)": tenure,
                "EMI": round(emi, 2),
                "Total Payment": round(total, 2),
                "Total Interest": round(interest, 2),
                "Interest %": round((interest / loan_amount) * 100, 1),
            })
    return pd.DataFrame(scenarios)

# ============================================================
# CORE: RISK SCORING
# ============================================================

def compute_risk(loan_amount, annual_income, interest_rate, loan_years):
    """Simple risk scoring model (0–100)."""
    if annual_income <= 0:
        return 100, "High"
    dti = (calculate_emi(loan_amount, interest_rate, loan_years * 12) * 12) / annual_income
    score = 0
    if dti < 0.3:   score += 40
    elif dti < 0.5: score += 20
    else:           score += 0

    if loan_years <= 10: score += 30
    elif loan_years <= 20: score += 20
    else: score += 10

    if interest_rate < 8:  score += 30
    elif interest_rate < 12: score += 15
    else: score += 5

    label = "Low" if score >= 70 else ("Medium" if score >= 40 else "High")
    return score, label

# ============================================================
# UI: SIDEBAR
# ============================================================

def sidebar_inputs():
    st.sidebar.markdown("## 🏦 LoanIQ Platform")
    st.sidebar.markdown("---")

    st.sidebar.markdown("### 💰 Loan Configuration")
    currency_key = st.sidebar.selectbox("Currency", list(CURRENCY_SYMBOLS.keys()), index=0)
    currency = CURRENCY_SYMBOLS[currency_key]

    loan_type = st.sidebar.selectbox(
        "Loan Type",
        ["Home / Mortgage", "Auto Loan", "Business Loan", "Personal Loan", "Education Loan", "Custom"]
    )

    # Defaults by loan type
    defaults = {
        "Home / Mortgage":  (5_000_000, 8.5, 20),
        "Auto Loan":        (800_000,   9.5, 5),
        "Business Loan":    (2_000_000, 11.0, 7),
        "Personal Loan":    (300_000,   14.0, 3),
        "Education Loan":   (500_000,   10.5, 5),
        "Custom":           (1_000_000, 10.0, 10),
    }
    def_amt, def_rate, def_yrs = defaults[loan_type]

    loan_amount = st.sidebar.number_input(
        f"Loan Amount ({currency})",
        min_value=10_000,
        max_value=100_000_000,
        value=def_amt,
        step=10_000
    )

    interest_rate = st.sidebar.slider(
        "Annual Interest Rate (%)",
        min_value=1.0, max_value=30.0,
        value=def_rate, step=0.1
    )

    loan_years = st.sidebar.slider(
        "Loan Tenure (Years)",
        min_value=1, max_value=40,
        value=def_yrs, step=1
    )

    st.sidebar.markdown("### ⚡ Extra Payments")
    extra_payment = st.sidebar.number_input(
        f"Extra Monthly Payment ({currency})",
        min_value=0,
        value=0,
        step=1000
    )

    frequency = st.sidebar.selectbox(
        "Payment Frequency",
        ["Monthly", "Quarterly", "Annual"]
    )

    st.sidebar.markdown("### 📊 Risk Analysis")
    annual_income = st.sidebar.number_input(
        f"Annual Income ({currency}) — for DTI",
        min_value=0,
        value=1_200_000,
        step=50_000
    )

    st.sidebar.markdown("### 🔄 Refinancing")
    refi_rate = st.sidebar.number_input(
        "Refinance Rate (%)",
        min_value=1.0,
        max_value=30.0,
        value=max(1.0, interest_rate - 1.5),
        step=0.1
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        "<small style='color:#475569;'>LoanIQ v2.0 | Enterprise Edition</small>",
        unsafe_allow_html=True
    )

    return (
        loan_amount, interest_rate, loan_years,
        extra_payment, frequency, currency,
        annual_income, refi_rate, loan_type
    )

# ============================================================
# UI: HEADER
# ============================================================

def render_header(loan_type, currency):
    st.markdown(f"""
    <div class="app-header">
        <span class="header-badge">Enterprise Edition</span>
        <h1>🏦 LoanIQ — Amortization Analytics</h1>
        <p>Production-grade EPM platform · {loan_type} · Currency: {currency}</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# UI: KPI CARDS ROW
# ============================================================

def render_kpi_row(df, df_base, loan_amount, base_emi, interest_rate, loan_years, extra_payment, currency):
    total_interest  = df["Interest"].sum()
    total_payment   = df["Payment"].sum()
    actual_periods  = len(df)
    original_periods = loan_years * 12

    base_total      = df_base["Payment"].sum()
    base_interest   = df_base["Interest"].sum()
    interest_saved  = base_interest - total_interest
    months_saved    = original_periods - actual_periods
    overpay_pct     = (total_interest / loan_amount) * 100

    st.markdown('<div class="section-title">📋 Executive KPI Summary</div>', unsafe_allow_html=True)

    cols = st.columns(5)
    cards = [
        ("Loan Amount",       fmt(loan_amount, currency),    f"{loan_years} yr tenure",     "accent-blue",   "🏠"),
        ("Monthly EMI",       fmt_plain(base_emi, currency), f"{interest_rate}% p.a.",       "accent-cyan",   "📅"),
        ("Total Interest",    fmt(total_interest, currency), f"{overpay_pct:.1f}% of loan",  "accent-amber",  "📈"),
        ("Total Repayment",   fmt(total_payment, currency),  f"vs {fmt(base_total, currency)} baseline", "accent-red", "💳"),
        ("Interest Saved",    fmt(interest_saved, currency), f"{months_saved} months early", "accent-green",  "💰"),
    ]

    for col, (label, value, sub, accent, icon) in zip(cols, cards):
        with col:
            st.markdown(f"""
            <div class="kpi-card {accent}">
                <span class="kpi-icon">{icon}</span>
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    cols2 = st.columns(4)
    cards2 = [
        ("Payoff Time",       f"{actual_periods} periods",  f"of {original_periods} planned",         "accent-blue",   "⏱️"),
        ("Interest %",        f"{overpay_pct:.1f}%",        "of principal as interest",               "accent-amber",  "📊"),
        ("Monthly Savings",   fmt(interest_saved/max(actual_periods,1), currency), "avg saved/period","accent-green",  "✅"),
        ("Effective Rate",    f"{interest_rate:.2f}%",       "nominal per annum",                     "accent-purple", "🎯"),
    ]
    for col, (label, value, sub, accent, icon) in zip(cols2, cards2):
        with col:
            st.markdown(f"""
            <div class="kpi-card {accent}">
                <span class="kpi-icon">{icon}</span>
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# CHARTS
# ============================================================

CHART_COLORS = {
    "blue":   "#2563EB",
    "cyan":   "#06B6D4",
    "green":  "#10B981",
    "amber":  "#F59E0B",
    "red":    "#EF4444",
    "purple": "#8B5CF6",
    "navy":   "#0F172A",
}

CHART_LAYOUT = dict(
    template="plotly_white",
    font=dict(family="Inter, sans-serif", size=12, color="#334155"),
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF",
    margin=dict(l=20, r=20, t=40, b=20),
    hoverlabel=dict(bgcolor="white", font_size=13, bordercolor="#E2E8F0"),
)


def chart_balance_decay(df, currency):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Remaining Balance"],
        mode="lines", fill="tozeroy",
        line=dict(color=CHART_COLORS["blue"], width=2.5),
        fillcolor="rgba(37,99,235,0.1)",
        name="Outstanding Balance",
        hovertemplate=f"Period %{{x}}<br>Balance: {currency}%{{y:,.0f}}<extra></extra>"
    ))
    fig.update_layout(**CHART_LAYOUT, title="📉 Loan Balance Decay Curve", height=320,
                      xaxis_title="Period", yaxis_title=f"Balance ({currency})")
    return fig


def chart_principal_interest_trend(df, currency):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Principal"],
        mode="lines", name="Principal",
        line=dict(color=CHART_COLORS["green"], width=2),
        hovertemplate=f"Period %{{x}}<br>Principal: {currency}%{{y:,.0f}}<extra></extra>"
    ))
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Interest"],
        mode="lines", name="Interest",
        line=dict(color=CHART_COLORS["red"], width=2, dash="dash"),
        hovertemplate=f"Period %{{x}}<br>Interest: {currency}%{{y:,.0f}}<extra></extra>"
    ))
    fig.update_layout(**CHART_LAYOUT, title="📊 Principal vs Interest Per Period", height=320,
                      xaxis_title="Period", yaxis_title=f"Amount ({currency})",
                      legend=dict(orientation="h", yanchor="bottom", y=1.02))
    return fig


def chart_cumulative_interest(df, currency):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Cumulative Interest"],
        mode="lines", fill="tozeroy",
        line=dict(color=CHART_COLORS["amber"], width=2.5),
        fillcolor="rgba(245,158,11,0.12)",
        name="Cumulative Interest",
        hovertemplate=f"Period %{{x}}<br>Cumulative: {currency}%{{y:,.0f}}<extra></extra>"
    ))
    fig.update_layout(**CHART_LAYOUT, title="📈 Cumulative Interest Paid Over Time", height=320,
                      xaxis_title="Period", yaxis_title=f"Amount ({currency})")
    return fig


def chart_distribution_donut(loan_amount, total_interest, currency):
    fig = go.Figure(go.Pie(
        labels=["Principal", "Interest"],
        values=[loan_amount, total_interest],
        hole=0.6,
        marker=dict(colors=[CHART_COLORS["blue"], CHART_COLORS["red"]],
                    line=dict(color="white", width=2)),
        textinfo="label+percent",
        hovertemplate=f"%{{label}}: {currency}%{{value:,.0f}}<extra></extra>"
    ))
    fig.update_layout(**CHART_LAYOUT, title="🍩 Payment Distribution", height=320,
                      showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.1))
    fig.add_annotation(text=f"{currency}{(loan_amount+total_interest)/1e5:.1f}L<br><span style='font-size:10px'>Total</span>",
                       x=0.5, y=0.5, showarrow=False, font=dict(size=14, color="#0F172A"))
    return fig


def chart_extra_payment_impact(df_base, df_extra, currency):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_base["Period"], y=df_base["Remaining Balance"],
        mode="lines", name="Without Extra Payments",
        line=dict(color=CHART_COLORS["red"], width=2, dash="dot"),
    ))
    fig.add_trace(go.Scatter(
        x=df_extra["Period"], y=df_extra["Remaining Balance"],
        mode="lines", name="With Extra Payments",
        line=dict(color=CHART_COLORS["green"], width=2.5),
        fill="tonexty", fillcolor="rgba(16,185,129,0.08)"
    ))
    fig.update_layout(**CHART_LAYOUT, title="⚡ Extra Payment Impact on Payoff", height=320,
                      xaxis_title="Period", yaxis_title=f"Balance ({currency})",
                      legend=dict(orientation="h", yanchor="bottom", y=1.02))
    return fig


def chart_scenario_heatmap(df_scen):
    pivot = df_scen.pivot(index="Tenure (Yrs)", columns="Rate (%)", values="Total Interest")
    fig = go.Figure(go.Heatmap(
        z=pivot.values,
        x=[f"{r}%" for r in pivot.columns],
        y=[f"{t} Yr" for t in pivot.index],
        colorscale=[[0, "#D1FAE5"], [0.5, "#FEF3C7"], [1, "#FEE2E2"]],
        text=[[f"{v/1e5:.1f}L" for v in row] for row in pivot.values],
        texttemplate="%{text}",
        showscale=True,
        hovertemplate="Rate: %{x}<br>Tenure: %{y}<br>Interest: %{text}<extra></extra>"
    ))
    fig.update_layout(**CHART_LAYOUT, title="🌡️ Interest Cost Heatmap (Rate × Tenure)", height=340)
    return fig


def chart_annual_payments(df):
    df = df.copy()
    df["Year"] = ((df["Period"] - 1) // 12) + 1
    annual = df.groupby("Year").agg({"Principal": "sum", "Interest": "sum"}).reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=annual["Year"], y=annual["Principal"],
                         name="Principal", marker_color=CHART_COLORS["blue"]))
    fig.add_trace(go.Bar(x=annual["Year"], y=annual["Interest"],
                         name="Interest", marker_color=CHART_COLORS["amber"]))
    fig.update_layout(**CHART_LAYOUT, title="📅 Annual Payment Breakdown",
                      barmode="stack", height=320, xaxis_title="Year", yaxis_title="Amount")
    return fig


def chart_refinance_comparison(df_current, df_refi, currency):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_current["Period"], y=df_current["Remaining Balance"],
        mode="lines", name="Current Rate",
        line=dict(color=CHART_COLORS["red"], width=2, dash="dot")
    ))
    fig.add_trace(go.Scatter(
        x=df_refi["Period"], y=df_refi["Remaining Balance"],
        mode="lines", name="Refinance Rate",
        line=dict(color=CHART_COLORS["green"], width=2.5)
    ))
    fig.update_layout(**CHART_LAYOUT, title="🔄 Refinancing Impact Simulation", height=320,
                      xaxis_title="Period", yaxis_title=f"Balance ({currency})",
                      legend=dict(orientation="h", yanchor="bottom", y=1.02))
    return fig

# ============================================================
# UI: FINANCIAL HEALTH INSIGHTS
# ============================================================

def render_insights(df, loan_amount, annual_income, interest_rate, loan_years, currency, extra_payment):
    total_interest = df["Interest"].sum()
    total_payment  = df["Payment"].sum()
    emi            = df["Payment"].iloc[0]
    overpay_pct    = (total_interest / loan_amount) * 100

    risk_score, risk_label = compute_risk(loan_amount, annual_income, interest_rate, loan_years)

    st.markdown('<div class="section-title">🧠 AI-Powered Financial Insights</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        # Insight 1: DTI
        if annual_income > 0:
            dti = (emi * 12) / annual_income * 100
            dti_color = "success" if dti < 30 else ("warn" if dti < 50 else "danger")
            dti_msg = "Healthy" if dti < 30 else ("Manageable" if dti < 50 else "Stressed")
            st.markdown(f"""
            <div class="insight-card {dti_color}">
                <b>📊 Debt-to-Income Ratio: {dti:.1f}% — {dti_msg}</b><br>
                <small>Your annual loan payments are {currency}{emi*12:,.0f} vs income of {currency}{annual_income:,.0f}.
                Keep DTI below 35% for financial health.</small>
            </div>""", unsafe_allow_html=True)

        # Insight 2: Interest burden
        burden_color = "success" if overpay_pct < 40 else ("warn" if overpay_pct < 70 else "danger")
        st.markdown(f"""
        <div class="insight-card {burden_color}">
            <b>💸 Interest Burden: {overpay_pct:.1f}% of Principal</b><br>
            <small>You'll pay {currency}{total_interest:,.0f} in interest on a {currency}{loan_amount:,.0f} loan.
            {"Great! Low interest burden." if overpay_pct < 40 else "Consider extra payments to reduce interest cost."}</small>
        </div>""", unsafe_allow_html=True)

        # Insight 3: Extra payment recommendation
        suggested_extra = loan_amount * 0.005
        rec_df  = build_schedule(loan_amount, interest_rate, loan_years, suggested_extra)
        rec_saved = total_interest - rec_df["Interest"].sum() if extra_payment == 0 else 0
        if rec_saved > 0:
            st.markdown(f"""
            <div class="insight-card success">
                <b>⚡ Smart Suggestion: Add {currency}{suggested_extra:,.0f}/month extra</b><br>
                <small>You could save {currency}{rec_saved:,.0f} in interest and pay off
                {loan_years*12 - len(rec_df)} months early with just 0.5% of principal as extra payment.</small>
            </div>""", unsafe_allow_html=True)

    with col2:
        # Risk gauge
        risk_cls = risk_label.lower()
        st.markdown(f"""
        <div class="kpi-card" style="text-align:center;">
            <div class="kpi-label">Financial Risk Score</div>
            <div class="kpi-value" style="font-size:3rem; color:{'#10B981' if risk_label=='Low' else '#F59E0B' if risk_label=='Medium' else '#EF4444'}">
                {risk_score}
            </div>
            <div style="margin-top:0.5rem">
                <span class="risk-{risk_cls}">{risk_label} Risk</span>
            </div>
            <div class="kpi-sub" style="margin-top:0.8rem">
                Score based on DTI, tenure<br>and interest rate
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# UI: AMORTIZATION TABLE
# ============================================================

def render_schedule_table(df, currency):
    st.markdown('<div class="section-title">📋 Detailed Amortization Schedule</div>', unsafe_allow_html=True)

    display_df = df.copy()
    for col in ["Payment", "Principal", "Interest", "Cumulative Interest", "Cumulative Principal", "Remaining Balance"]:
        display_df[col] = display_df[col].apply(lambda x: f"{currency}{x:,.2f}")

    search = st.text_input("🔍 Filter by period number", "")
    if search:
        try:
            p = int(search)
            display_df = display_df[display_df["Period"] == p]
        except ValueError:
            pass

    st.dataframe(display_df, use_container_width=True, height=400)

# ============================================================
# UI: SCENARIO COMPARISON TABLE
# ============================================================

def render_scenario_table(loan_amount, interest_rate, loan_years, currency):
    st.markdown('<div class="section-title">🔀 Multi-Scenario Comparison</div>', unsafe_allow_html=True)
    df_scen = multi_scenario(loan_amount, interest_rate, loan_years, currency)

    styled = df_scen.copy()
    styled["EMI"]          = styled["EMI"].apply(lambda x: f"{currency}{x:,.2f}")
    styled["Total Payment"]= styled["Total Payment"].apply(lambda x: f"{currency}{x:,.2f}")
    styled["Total Interest"]= styled["Total Interest"].apply(lambda x: f"{currency}{x:,.2f}")
    styled["Interest %"]   = styled["Interest %"].apply(lambda x: f"{x}%")

    st.dataframe(styled, use_container_width=True)
    return df_scen

# ============================================================
# EXPORT FUNCTIONS
# ============================================================

def export_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")

def export_excel(df: pd.DataFrame, loan_amount, base_emi, interest_rate, loan_years) -> bytes:
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        # Summary sheet
        summary_data = {
            "Parameter": ["Loan Amount", "Annual Interest Rate", "Tenure (Years)", "Monthly EMI",
                          "Total Interest", "Total Payment", "Interest %"],
            "Value": [
                loan_amount, f"{interest_rate}%", loan_years,
                round(base_emi, 2),
                round(df["Interest"].sum(), 2),
                round(df["Payment"].sum(), 2),
                f"{(df['Interest'].sum()/loan_amount)*100:.2f}%"
            ]
        }
        pd.DataFrame(summary_data).to_excel(writer, sheet_name="Summary", index=False)
        df.to_excel(writer, sheet_name="Amortization Schedule", index=False)
    return buf.getvalue()

# ============================================================
# MAIN APP
# ============================================================

def main():
    load_css()

    # --- INPUTS ---
    (loan_amount, interest_rate, loan_years,
     extra_payment, frequency, currency,
     annual_income, refi_rate, loan_type) = sidebar_inputs()

    # --- CALCULATIONS ---
    months   = loan_years * 12
    base_emi = calculate_emi(loan_amount, interest_rate, months)

    df      = build_schedule(loan_amount, interest_rate, loan_years, extra_payment, frequency)
    df_base = build_no_extra_schedule(loan_amount, interest_rate, loan_years, frequency)
    df_refi = build_schedule(loan_amount, refi_rate, loan_years, extra_payment, frequency)

    total_interest = df["Interest"].sum()
    total_payment  = df["Payment"].sum()

    # --- HEADER ---
    render_header(loan_type, currency)

    # --- KPI ROW ---
    render_kpi_row(df, df_base, loan_amount, base_emi, interest_rate, loan_years, extra_payment, currency)

    # ============================================================
    # TABS
    # ============================================================
    tabs = st.tabs([
        "📊 Dashboard",
        "📈 Analytics",
        "🔀 Scenarios",
        "🔄 Refinancing",
        "📋 Schedule",
        "🧠 Insights",
        "⬇️ Export"
    ])

    # ----------------------------------------------------------
    # TAB 1: DASHBOARD
    # ----------------------------------------------------------
    with tabs[0]:
        st.markdown('<div class="section-title">📊 Executive Dashboard</div>', unsafe_allow_html=True)

        r1c1, r1c2 = st.columns(2)
        with r1c1:
            st.plotly_chart(chart_balance_decay(df, currency), use_container_width=True)
        with r1c2:
            st.plotly_chart(chart_distribution_donut(loan_amount, total_interest, currency), use_container_width=True)

        r2c1, r2c2 = st.columns(2)
        with r2c1:
            st.plotly_chart(chart_principal_interest_trend(df, currency), use_container_width=True)
        with r2c2:
            st.plotly_chart(chart_annual_payments(df), use_container_width=True)

    # ----------------------------------------------------------
    # TAB 2: ANALYTICS
    # ----------------------------------------------------------
    with tabs[1]:
        st.markdown('<div class="section-title">📈 Advanced Financial Analytics</div>', unsafe_allow_html=True)

        st.plotly_chart(chart_cumulative_interest(df, currency), use_container_width=True)

        if extra_payment > 0:
            st.plotly_chart(chart_extra_payment_impact(df_base, df, currency), use_container_width=True)
        else:
            st.info("💡 Set an extra monthly payment in the sidebar to see prepayment impact analysis.")

        # Payoff forecast table
        st.markdown('<div class="section-title">📅 Payoff Forecast</div>', unsafe_allow_html=True)
        milestones = [0.25, 0.50, 0.75, 1.0]
        forecast_rows = []
        for pct in milestones:
            target = loan_amount * (1 - pct)
            row = df[df["Remaining Balance"] <= target]
            period = int(row["Period"].iloc[0]) if len(row) > 0 else len(df)
            forecast_rows.append({
                "Milestone": f"{int(pct*100)}% Paid Off",
                "Period": period,
                "Remaining Balance": f"{currency}{max(0, loan_amount*(1-pct)):,.0f}",
                "Interest Paid So Far": f"{currency}{df[df['Period']<=period]['Interest'].sum():,.0f}"
            })
        st.dataframe(pd.DataFrame(forecast_rows), use_container_width=True)

    # ----------------------------------------------------------
    # TAB 3: SCENARIOS
    # ----------------------------------------------------------
    with tabs[2]:
        df_scen = render_scenario_table(loan_amount, interest_rate, loan_years, currency)
        st.plotly_chart(chart_scenario_heatmap(df_scen), use_container_width=True)

        # Bar comparison — EMI by rate
        fig_emi = px.bar(
            df_scen[df_scen["Tenure (Yrs)"] == loan_years],
            x="Rate (%)", y="EMI",
            color="EMI",
            color_continuous_scale=["#D1FAE5", "#FEF3C7", "#FEE2E2"],
            title="💳 EMI vs Interest Rate (Current Tenure)",
            text="EMI",
        )
        fig_emi.update_traces(texttemplate=f"{currency}%{{text:,.0f}}", textposition="outside")
        fig_emi.update_layout(**CHART_LAYOUT, height=320, coloraxis_showscale=False)
        st.plotly_chart(fig_emi, use_container_width=True)

    # ----------------------------------------------------------
    # TAB 4: REFINANCING
    # ----------------------------------------------------------
    with tabs[3]:
        st.markdown('<div class="section-title">🔄 Refinancing Calculator</div>', unsafe_allow_html=True)

        refi_interest = df_refi["Interest"].sum()
        current_interest = total_interest
        refi_savings = current_interest - refi_interest

        rc1, rc2, rc3 = st.columns(3)
        with rc1:
            st.markdown(f"""
            <div class="kpi-card accent-red">
                <span class="kpi-icon">📌</span>
                <div class="kpi-label">Current Rate Cost</div>
                <div class="kpi-value">{fmt(current_interest, currency)}</div>
                <div class="kpi-sub">@ {interest_rate}% p.a.</div>
            </div>""", unsafe_allow_html=True)
        with rc2:
            st.markdown(f"""
            <div class="kpi-card accent-blue">
                <span class="kpi-icon">🔄</span>
                <div class="kpi-label">Refi Rate Cost</div>
                <div class="kpi-value">{fmt(refi_interest, currency)}</div>
                <div class="kpi-sub">@ {refi_rate}% p.a.</div>
            </div>""", unsafe_allow_html=True)
        with rc3:
            st.markdown(f"""
            <div class="kpi-card accent-green">
                <span class="kpi-icon">💰</span>
                <div class="kpi-label">Refinancing Savings</div>
                <div class="kpi-value">{fmt(refi_savings, currency)}</div>
                <div class="kpi-sub">{"✅ Refinancing recommended" if refi_savings > 0 else "⚠️ Current rate is better"}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.plotly_chart(chart_refinance_comparison(df, df_refi, currency), use_container_width=True)

    # ----------------------------------------------------------
    # TAB 5: SCHEDULE
    # ----------------------------------------------------------
    with tabs[4]:
        render_schedule_table(df, currency)

    # ----------------------------------------------------------
    # TAB 6: INSIGHTS
    # ----------------------------------------------------------
    with tabs[5]:
        render_insights(df, loan_amount, annual_income, interest_rate, loan_years, currency, extra_payment)

    # ----------------------------------------------------------
    # TAB 7: EXPORT
    # ----------------------------------------------------------
    with tabs[6]:
        st.markdown('<div class="section-title">⬇️ Export & Download</div>', unsafe_allow_html=True)

        ec1, ec2 = st.columns(2)

        with ec1:
            st.markdown("#### 📄 CSV Export")
            st.markdown("Download the full amortization schedule as a CSV file.")
            st.download_button(
                label="⬇️ Download CSV",
                data=export_csv(df),
                file_name="amortization_schedule.csv",
                mime="text/csv",
                use_container_width=True
            )

        with ec2:
            st.markdown("#### 📊 Excel Export")
            st.markdown("Download a multi-sheet Excel workbook with summary + schedule.")
            st.download_button(
                label="⬇️ Download Excel (.xlsx)",
                data=export_excel(df, loan_amount, base_emi, interest_rate, loan_years),
                file_name="loan_analytics_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

        st.markdown("---")
        st.markdown("#### 📋 Data Preview")
        st.dataframe(df.head(24), use_container_width=True)

    # ----------------------------------------------------------
    # FOOTER
    # ----------------------------------------------------------
    st.markdown("""
    <div class="footer">
        🏦 LoanIQ Enterprise Amortization Platform v2.0<br>
        Built with Python · Streamlit · Plotly · Pandas<br>
        <small>Replacing Excel-based amortization with real-time analytics</small>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
