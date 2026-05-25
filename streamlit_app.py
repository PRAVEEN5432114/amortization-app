import streamlit as st
import pandas as pd

st.title("Loan Amortization Calculator")

loan_amount = st.number_input("Loan Amount", value=100000)
interest_rate = st.number_input("Annual Interest Rate (%)", value=8.5)
loan_years = st.number_input("Loan Term (Years)", value=10)

monthly_rate = interest_rate / 100 / 12
months = loan_years * 12

monthly_payment = (
    loan_amount *
    (monthly_rate * (1 + monthly_rate) ** months) /
    ((1 + monthly_rate) ** months - 1)
)

st.subheader(f"Monthly Payment: ₹{monthly_payment:,.2f}")

schedule = []

balance = loan_amount

for month in range(1, months + 1):
    interest = balance * monthly_rate
    principal = monthly_payment - interest
    balance -= principal

    schedule.append([
        month,
        round(monthly_payment, 2),
        round(principal, 2),
        round(interest, 2),
        round(balance if balance > 0 else 0, 2)
    ])

df = pd.DataFrame(
    schedule,
    columns=[
        "Month",
        "Payment",
        "Principal",
        "Interest",
        "Remaining Balance"
    ]
)

st.dataframe(df)
