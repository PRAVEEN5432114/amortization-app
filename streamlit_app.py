```python
# ============================================================
# ENTERPRISE LOAN AMORTIZATION & FINANCIAL ANALYTICS PLATFORM
# Production-Ready | EPM-Grade | Streamlit + Plotly
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import io

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LoanIQ Enterprise",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

def load_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {
        --bg-main: #F8FAFC;
        --bg-card: #FFFFFF;
        --bg-sidebar: #0F172A;

        --text-primary: #0F172A;
        --text-secondary: #475569;
        --text-muted: #94A3B8;

        --blue: #2563EB;
        --cyan: #06B6D4;
        --green: #10B981;
        --amber: #F59E0B;
        --red: #EF4444;
        --purple: #8B5CF6;

        --border: #E2E8F0;

        --shadow-sm: 0 2px 8px rgba(15,23,42,0.04);
        --shadow-md: 0 8px 24px rgba(15,23,42,0.08);
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
    }

    body {
        background: var(--bg-main);
    }

    .main {
        background: var(--bg-main);
    }

    /* Sidebar */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #0F172A 0%,
            #111827 100%
        );
    }

    [data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }

    /* Header */

    .app-header {
        background:
            linear-gradient(
                135deg,
                #0F172A 0%,
                #1E293B 50%,
                #0F172A 100%
            );

        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 2rem;

        box-shadow: var(--shadow-md);
    }

    .app-header h1 {
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }

    .app-header p {
        color: #CBD5E1;
        margin-top: 0.5rem;
    }

    /* Section */

    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        color: var(--text-primary);
    }

    /* Equal KPI heights */

    div[data-testid="column"] {
        display: flex;
    }

    div[data-testid="column"] > div {
        width: 100%;
    }

    /* KPI */

    .kpi-card {
        background: white;
        border: 1px solid var(--border);

        border-radius: 20px;

        padding: 1.25rem;

        height: 100%;
        min-height: 190px;

        display: flex;
        flex-direction: column;
        justify-content: space-between;

        box-shadow: var(--shadow-sm);

        transition: 0.2s ease;
    }

    .kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-md);
    }

    .accent-blue {
        border-top: 4px solid var(--blue);
    }

    .accent-green {
        border-top: 4px solid var(--green);
    }

    .accent-amber {
        border-top: 4px solid var(--amber);
    }

    .accent-red {
        border-top: 4px solid var(--red);
    }

    .accent-cyan {
        border-top: 4px solid var(--cyan);
    }

    .kpi-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: var(--text-muted);
    }

    .kpi-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: var(--text-primary);
        font-family: 'JetBrains Mono', monospace;
        margin-top: 0.6rem;
    }

    .kpi-sub {
        font-size: 0.82rem;
        color: var(--text-secondary);
        margin-top: 0.8rem;
    }

    /* Metric */

    div[data-testid="metric-container"] {
        background: white;
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1rem;
        box-shadow: var(--shadow-sm);
    }

    /* Tabs */

    .stTabs [data-baseweb="tab-list"] {
        background: white;
        border-radius: 14px;
        border: 1px solid var(--border);
        padding: 5px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        font-weight: 600;
    }

    /* Footer */

    .footer {
        margin-top: 3rem;
        padding: 2rem;
        text-align: center;
        color: #94A3B8;
        border-top: 1px solid var(--border);
    }

    </style>
    """, unsafe_allow_html=True)

load_css()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏦 LoanIQ Enterprise")

currency = st.sidebar.selectbox(
    "Currency",
    ["₹", "$", "€", "£"]
)

loan_amount = st.sidebar.number_input(
    "Loan Amount",
    min_value=10000,
    value=5000000,
    step=10000
)

interest_rate = st.sidebar.slider(
    "Interest Rate (%)",
    1.0,
    30.0,
    8.5
)

loan_years = st.sidebar.slider(
    "Loan Tenure (Years)",
    1,
    40,
    20
)

extra_payment = st.sidebar.number_input(
    "Extra Monthly Payment",
    min_value=0,
    value=0,
    step=1000
)

# ============================================================
# EMI CALCULATION
# ============================================================

months = loan_years * 12
monthly_rate = interest_rate / 100 / 12

if monthly_rate == 0:
    emi = loan_amount / months
else:
    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

emi += extra_payment

# ============================================================
# AMORTIZATION SCHEDULE
# ============================================================

balance = loan_amount

schedule = []

total_interest = 0
total_payment = 0

for month in range(1, months + 1):

    interest_payment = balance * monthly_rate

    principal_payment = emi - interest_payment

    if principal_payment > balance:
        principal_payment = balance
        emi_actual = principal_payment + interest_payment
    else:
        emi_actual = emi

    balance -= principal_payment

    total_interest += interest_payment
    total_payment += emi_actual

    schedule.append({
        "Month": month,
        "Payment": round(emi_actual, 2),
        "Principal": round(principal_payment, 2),
        "Interest": round(interest_payment, 2),
        "Balance": round(max(balance, 0), 2)
    })

    if balance <= 0:
        break

df = pd.DataFrame(schedule)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="app-header">
    <h1>🏦 LoanIQ Enterprise Platform</h1>
    <p>Modern Enterprise Amortization & Financial Analytics Platform</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# KPI SECTION
# ============================================================

st.markdown(
    '<div class="section-title">📊 Executive KPI Dashboard</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

kpis = [
    ("Loan Amount", f"{currency}{loan_amount:,.0f}", "Principal borrowed", "accent-blue"),
    ("Monthly EMI", f"{currency}{emi:,.0f}", "Monthly payment", "accent-cyan"),
    ("Total Interest", f"{currency}{total_interest:,.0f}", "Interest payable", "accent-amber"),
    ("Total Payment", f"{currency}{total_payment:,.0f}", "Overall repayment", "accent-red"),
    ("Loan Months", f"{len(df)}", "Actual payoff period", "accent-green")
]

for col, item in zip([col1, col2, col3, col4, col5], kpis):

    label, value, sub, accent = item

    with col:
        st.markdown(f"""
        <div class="kpi-card {accent}">
            <div>
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
            </div>
            <div class="kpi-sub">{sub}</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard",
    "📈 Analytics",
    "📋 Schedule",
    "⬇️ Export"
])

# ============================================================
# DASHBOARD
# ============================================================

with tab1:

    st.markdown(
        '<div class="section-title">Financial Dashboard</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        fig_balance = px.area(
            df,
            x="Month",
            y="Balance",
            title="Outstanding Balance"
        )

        fig_balance.update_layout(
            template="plotly_white",
            height=350
        )

        st.plotly_chart(fig_balance, use_container_width=True)

    with c2:

        pie_df = pd.DataFrame({
            "Category": ["Principal", "Interest"],
            "Value": [loan_amount, total_interest]
        })

        fig_pie = px.pie(
            pie_df,
            names="Category",
            values="Value",
            hole=0.6,
            title="Principal vs Interest"
        )

        fig_pie.update_layout(
            template="plotly_white",
            height=350
        )

        st.plotly_chart(fig_pie, use_container_width=True)

# ============================================================
# ANALYTICS
# ============================================================

with tab2:

    st.markdown(
        '<div class="section-title">Payment Analytics</div>',
        unsafe_allow_html=True
    )

    c3, c4 = st.columns(2)

    with c3:

        fig_trend = go.Figure()

        fig_trend.add_trace(
            go.Scatter(
                x=df["Month"],
                y=df["Principal"],
                name="Principal"
            )
        )

        fig_trend.add_trace(
            go.Scatter(
                x=df["Month"],
                y=df["Interest"],
                name="Interest"
            )
        )

        fig_trend.update_layout(
            template="plotly_white",
            title="Principal vs Interest Trend",
            height=350
        )

        st.plotly_chart(fig_trend, use_container_width=True)

    with c4:

        df["Cumulative Interest"] = df["Interest"].cumsum()

        fig_interest = px.area(
            df,
            x="Month",
            y="Cumulative Interest",
            title="Cumulative Interest Paid"
        )

        fig_interest.update_layout(
            template="plotly_white",
            height=350
        )

        st.plotly_chart(fig_interest, use_container_width=True)

# ============================================================
# SCHEDULE
# ============================================================

with tab3:

    st.markdown(
        '<div class="section-title">Detailed Amortization Schedule</div>',
        unsafe_allow_html=True
    )

    st.dataframe(df, use_container_width=True)

# ============================================================
# EXPORT
# ============================================================

with tab4:

    st.markdown(
        '<div class="section-title">Export Reports</div>',
        unsafe_allow_html=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download CSV",
        csv,
        "amortization_schedule.csv",
        "text/csv"
    )

    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Amortization")

    st.download_button(
        "⬇️ Download Excel",
        excel_buffer.getvalue(),
        "loan_report.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    LoanIQ Enterprise • Built with Streamlit + Plotly + Pandas
</div>
""", unsafe_allow_html=True)
```
