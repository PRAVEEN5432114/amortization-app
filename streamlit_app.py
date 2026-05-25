# ============================================================
# ✅ ENTERPRISE DASHBOARD LAYOUT (NO TABS)
# ============================================================

sh("📊 Master Dashboard")

# ✅ KPI already rendered above

# -----------------------------
# ✅ ROW 1 → MAIN CHART + SIDE PANEL
# -----------------------------
col1, col2 = st.columns([3,1])

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_pi_trend(df, sym), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_balance_decay(df, sym), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# ✅ ROW 2 → HEATMAP + DONUT
# -----------------------------
col3, col4 = st.columns([1,1])

with col3:
    df_scen = multi_scenario(loan_amount, interest_rate, loan_years)
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_heatmap(df_scen), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_donut(loan_amount, total_interest, sym), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# ✅ ROW 3 → CUMULATIVE + STACK
# -----------------------------
col5, col6 = st.columns(2)

with col5:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_cumulative(df, sym), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_annual_stack(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# ✅ EXTRA PAYMENT IMPACT
# -----------------------------
