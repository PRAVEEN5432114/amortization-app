import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Enterprise Amortization Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

custom_css = """
<style>

.main {
    background-color: #F8FAFC;
}

h1, h2, h3 {
    color: #0F172A;
}

div[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #E2E8F0;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------

st.sidebar.title("Loan Configuration")

loan_amount = st.sidebar.number_input(
    "Loan Amount (₹)",
    min_value=1000,
    value=500000,
    step=10000
)

interest_rate = st.sidebar.slider(
    "Annual Interest Rate (%)",
    min_value=1.0,
    max_value=25.0,
    value=8.5
)

loan_years = st.sidebar.slider(
    "Loan Tenure (Years)",
    min_value=1,
    max_value=40,
    value=15
)

extra_payment = st.sidebar.number_input(
    "Extra Monthly Payment (₹)",
    min_value=0,
    value=0,
    step=1000
)

# ---------------------------------------------------
# EMI CALCULATIONS
# ---------------------------------------------------

monthly_rate = interest_rate / 100 / 12
months = loan_years * 12

base_emi = (
    loan_amount *
    (monthly_rate * (1 + monthly_rate) ** months)
    /
    ((1 + monthly_rate) ** months - 1)
)

monthly_payment = base_emi + extra_payment

# ---------------------------------------------------
# AMORTIZATION SCHEDULE
# ---------------------------------------------------

schedule = []

balance = loan_amount
total_interest = 0
total_payment = 0

for month in range(1, months + 1):

    interest_payment = balance * monthly_rate

    principal_payment = monthly_payment - interest_payment

    # Prevent negative balance
    if principal_payment > balance:
        principal_payment = balance
        monthly_payment = principal_payment + interest_payment

    balance -= principal_payment

    total_interest += interest_payment
    total_payment += monthly_payment

    schedule.append({
        "Month": month,
        "Payment": round(monthly_payment, 2),
        "Principal": round(principal_payment, 2),
        "Interest": round(interest_payment, 2),
        "Remaining Balance": round(max(balance, 0), 2)
    })

    if balance <= 0:
        break

# ---------------------------------------------------
# DATAFRAME
# ---------------------------------------------------

df = pd.DataFrame(schedule)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("📊 Enterprise Loan Amortization Analytics")

st.markdown("""
Modern enterprise-grade amortization analytics platform replacing traditional Excel-based workflows.
""")

# ---------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------

st.subheader("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Monthly EMI",
        f"₹{base_emi:,.2f}"
    )

with col2:
    st.metric(
        "Total Interest Paid",
        f"₹{total_interest:,.2f}"
    )

with col3:
    st.metric(
        "Total Payment",
        f"₹{total_payment:,.2f}"
    )

with col4:
    overpayment_percent = (total_interest / loan_amount) * 100

    st.metric(
        "Overpayment %",
        f"{overpayment_percent:.2f}%"
    )

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

st.subheader("Financial Dashboard")

dashboard_col1, dashboard_col2 = st.columns(2)

# Loan Balance Chart

with dashboard_col1:

    fig_balance = px.line(
        df,
        x="Month",
        y="Remaining Balance",
        title="Outstanding Loan Balance"
    )

    fig_balance.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig_balance, use_container_width=True)

# Principal vs Interest Pie

with dashboard_col2:

    pie_df = pd.DataFrame({
        "Category": ["Principal", "Interest"],
        "Amount": [loan_amount, total_interest]
    })

    fig_pie = px.pie(
        pie_df,
        names="Category",
        values="Amount",
        title="Principal vs Interest Distribution"
    )

    fig_pie.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig_pie, use_container_width=True)

# ---------------------------------------------------
# PAYMENT ANALYTICS
# ---------------------------------------------------

st.subheader("Payment Analytics")

analytics_col1, analytics_col2 = st.columns(2)

# Principal vs Interest Trend

with analytics_col1:

    fig_trend = go.Figure()

    fig_trend.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Principal"],
            mode="lines",
            name="Principal"
        )
    )

    fig_trend.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Interest"],
            mode="lines",
            name="Interest"
        )
    )

    fig_trend.update_layout(
        title="Principal vs Interest Payments",
        template="plotly_white"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

# Cumulative Interest

with analytics_col2:

    df["Cumulative Interest"] = df["Interest"].cumsum()

    fig_area = px.area(
        df,
        x="Month",
        y="Cumulative Interest",
        title="Cumulative Interest Paid"
    )

    fig_area.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig_area, use_container_width=True)

# ---------------------------------------------------
# OVERPAYMENT ANALYSIS
# ---------------------------------------------------

st.subheader("Overpayment Analysis")

interest_savings = 0

if extra_payment > 0:

    original_total_payment = base_emi * months

    interest_savings = original_total_payment - total_payment

col5, col6, col7 = st.columns(3)

with col5:
    st.metric(
        "Loan Amount",
        f"₹{loan_amount:,.2f}"
    )

with col6:
    st.metric(
        "Interest Paid",
        f"₹{total_interest:,.2f}"
    )

with col7:
    st.metric(
        "Savings from Extra Payments",
        f"₹{interest_savings:,.2f}"
    )

# ---------------------------------------------------
# AMORTIZATION TABLE
# ---------------------------------------------------

st.subheader("Detailed Amortization Schedule")

st.dataframe(
    df,
    use_container_width=True
)

# ---------------------------------------------------
# DOWNLOAD SECTION
# ---------------------------------------------------

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Amortization Schedule CSV",
    data=csv,
    file_name="amortization_schedule.csv",
    mime="text/csv"
)

# ---------------------------------------------------
# BUSINESS VALUE SECTION
# ---------------------------------------------------

st.markdown("---")

st.subheader("Why This App Instead of Excel?")

st.markdown("""
### Problems with Traditional Excel Amortization Models

- Manual formula errors
- Broken references
- No interactive analytics
- Difficult scenario planning
- Poor executive dashboards
- No centralized financial reporting
- Limited scalability

### Benefits of This Enterprise Web App

✅ Real-time amortization analytics  
✅ Interactive executive dashboards  
✅ Automated calculations  
✅ Downloadable reports  
✅ Overpayment analysis  
✅ Better financial decision-making  
✅ Modern enterprise UI/UX  
✅ Faster loan simulations  
""")
