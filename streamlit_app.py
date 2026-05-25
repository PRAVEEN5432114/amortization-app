import streamlit as st
    original_total = original_payment * months
    new_total = total_payment

    interest_savings = original_total - new_total

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
        "Potential Savings",
        f"₹{interest_savings:,.2f}"
    )

# ----------------------------------------------------
# AMORTIZATION TABLE
# ----------------------------------------------------

st.subheader("Detailed Amortization Schedule")

st.dataframe(df, use_container_width=True)

# ----------------------------------------------------
# DOWNLOAD SECTION
# ----------------------------------------------------

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Amortization Schedule CSV",
    data=csv,
    file_name='amortization_schedule.csv',
    mime='text/csv'
)

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("---")

st.markdown(
    """
    ### Enterprise Benefits Over Excel

    ✅ Centralized financial analytics  
    ✅ Interactive dashboards  
    ✅ Error-free calculations  
    ✅ Better executive reporting  
    ✅ Faster loan simulations  
    ✅ Modern enterprise UI/UX  
    ✅ Automated amortization engine  
    ✅ Scalable for multiple loan portfolios  
    """
)
