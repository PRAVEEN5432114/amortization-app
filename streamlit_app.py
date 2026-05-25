# ============================================================
# LOANIQ — ENTERPRISE LOAN AMORTIZATION & ANALYTICS PLATFORM
# Version 3.0 | Bloomberg-grade UI | EPM-class Analytics
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LoanIQ | Enterprise Finance Analytics",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DESIGN SYSTEM — ENTERPRISE FINTECH CSS
# ============================================================

def load_css():
    st.markdown("""
    <style>

    /* =====================================================
       FONTS
    ===================================================== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* =====================================================
       CSS DESIGN TOKENS
    ===================================================== */
    :root {
        --navy:        #0F172A;
        --blue:        #2563EB;
        --blue-light:  #3B82F6;
        --blue-pale:   #EFF6FF;
        --cyan:        #06B6D4;
        --cyan-pale:   #ECFEFF;
        --green:       #10B981;
        --green-pale:  #ECFDF5;
        --amber:       #F59E0B;
        --amber-pale:  #FFFBEB;
        --red:         #EF4444;
        --red-pale:    #FEF2F2;
        --purple:      #8B5CF6;
        --purple-pale: #F5F3FF;

        --bg-page:     #F1F5F9;
        --bg-card:     #FFFFFF;
        --bg-sidebar:  #0F172A;

        --text-primary:   #0F172A;
        --text-secondary: #475569;
        --text-muted:     #94A3B8;
        --text-white:     #FFFFFF;
        --text-white-dim: #CBD5E1;

        --border:      #E2E8F0;
        --border-dark: #CBD5E1;

        --radius-sm:   8px;
        --radius-md:   12px;
        --radius-lg:   20px;

        --shadow-sm:   0 1px 4px rgba(15,23,42,0.06);
        --shadow-md:   0 4px 16px rgba(15,23,42,0.08);
        --shadow-lg:   0 8px 32px rgba(15,23,42,0.12);
        --shadow-hover:0 12px 40px rgba(15,23,42,0.16);

        --font-ui:     'Inter', system-ui, sans-serif;
        --font-mono:   'JetBrains Mono', 'Fira Code', monospace;
    }

    /* =====================================================
       GLOBAL RESET
    ===================================================== */
    html, body,
    [class*="css"],
    .stApp,
    .stApp > header,
    section[data-testid="stSidebar"] > div {
        font-family: var(--font-ui) !important;
    }

    .stApp { background-color: var(--bg-page) !important; }

    .block-container {
        padding: 1.5rem 2rem 3rem !important;
        max-width: 100% !important;
    }

    h1, h2, h3, h4 { color: var(--text-primary) !important; }
    p, li { color: var(--text-secondary); }

    /* =====================================================
       HEADER BANNER
    ===================================================== */
    .app-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E3358 45%, #0F2057 100%);
        border: 1px solid rgba(37,99,235,0.4);
        border-radius: var(--radius-lg);
        padding: 2.2rem 2.8rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .app-header::after {
        content: '';
        position: absolute;
        top: -80px; right: -80px;
        width: 320px; height: 320px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(37,99,235,0.18) 0%, transparent 65%);
        pointer-events: none;
    }
    .app-header::before {
        content: '';
        position: absolute;
        bottom: -60px; left: 30%;
        width: 200px; height: 200px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(6,182,212,0.12) 0%, transparent 65%);
        pointer-events: none;
    }
    .app-header-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(37,99,235,0.25);
        border: 1px solid rgba(37,99,235,0.5);
        color: #93C5FD;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 0.8rem;
    }
    .app-header h1 {
        color: #FFFFFF !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin: 0 0 0.4rem 0 !important;
        letter-spacing: -0.8px;
        line-height: 1.15;
    }
    .app-header p {
        color: #94A3B8 !important;
        font-size: 0.92rem;
        margin: 0;
        line-height: 1.6;
    }
    .header-stats {
        display: flex;
        gap: 2rem;
        margin-top: 1.4rem;
        padding-top: 1.2rem;
        border-top: 1px solid rgba(255,255,255,0.08);
    }
    .header-stat-item { display: flex; flex-direction: column; }
    .header-stat-label {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        color: #64748B;
        margin-bottom: 2px;
    }
    .header-stat-value {
        font-family: var(--font-mono);
        font-size: 1.1rem;
        font-weight: 600;
        color: #FFFFFF;
    }

    /* =====================================================
       KPI CARD SYSTEM — EQUAL HEIGHT, FLEXBOX
    ===================================================== */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 14px;
        margin-bottom: 14px;
    }
    .kpi-grid-4 {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-bottom: 2rem;
    }

    .kpi-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 1.4rem 1.5rem 1.3rem;
        box-shadow: var(--shadow-sm);
        transition: transform 0.22s cubic-bezier(0.4,0,0.2,1),
                    box-shadow 0.22s cubic-bezier(0.4,0,0.2,1);
        display: flex;
        flex-direction: column;
        min-height: 148px;
        position: relative;
        overflow: hidden;
    }
    .kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-hover);
    }
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: var(--radius-lg) var(--radius-lg) 0 0;
    }
    .kpi-card.kpi-blue::before   { background: var(--blue); }
    .kpi-card.kpi-green::before  { background: var(--green); }
    .kpi-card.kpi-amber::before  { background: var(--amber); }
    .kpi-card.kpi-red::before    { background: var(--red); }
    .kpi-card.kpi-cyan::before   { background: var(--cyan); }
    .kpi-card.kpi-purple::before { background: var(--purple); }

    .kpi-card-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        margin-bottom: auto;
    }
    .kpi-icon-wrap {
        width: 38px; height: 38px;
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.1rem;
        flex-shrink: 0;
    }
    .kpi-blue   .kpi-icon-wrap { background: var(--blue-pale);   }
    .kpi-green  .kpi-icon-wrap { background: var(--green-pale);  }
    .kpi-amber  .kpi-icon-wrap { background: var(--amber-pale);  }
    .kpi-red    .kpi-icon-wrap { background: var(--red-pale);    }
    .kpi-cyan   .kpi-icon-wrap { background: var(--cyan-pale);   }
    .kpi-purple .kpi-icon-wrap { background: var(--purple-pale); }

    .kpi-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: var(--text-muted);
        margin: 1rem 0 0.3rem;
        line-height: 1;
    }
    .kpi-value {
        font-family: var(--font-mono);
        font-size: 1.6rem;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.15;
        letter-spacing: -0.5px;
    }
    .kpi-sub {
        font-size: 0.74rem;
        color: var(--text-muted);
        margin-top: 0.35rem;
        line-height: 1.4;
    }
    .kpi-sub.pos { color: var(--green); font-weight: 600; }
    .kpi-sub.neg { color: var(--red);   font-weight: 600; }

    /* =====================================================
       SECTION HEADERS
    ===================================================== */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin: 2rem 0 1.1rem;
        padding-bottom: 0.7rem;
        border-bottom: 1.5px solid var(--border);
    }
    .section-header-icon {
        width: 30px; height: 30px;
        background: var(--blue-pale);
        border-radius: 8px;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.95rem;
    }
    .section-header-text {
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.2px;
    }
    .section-header-count {
        margin-left: auto;
        font-size: 0.72rem;
        font-weight: 600;
        color: var(--text-muted);
        background: #F1F5F9;
        padding: 3px 10px;
        border-radius: 20px;
    }

    /* =====================================================
       INSIGHT CARDS
    ===================================================== */
    .insight-card {
        border-radius: var(--radius-md);
        padding: 1rem 1.25rem;
        margin-bottom: 0.85rem;
        border-left: 4px solid transparent;
        position: relative;
    }
    .insight-card b {
        font-size: 0.88rem;
        font-weight: 700;
        display: block;
        margin-bottom: 0.3rem;
    }
    .insight-card small {
        font-size: 0.8rem;
        line-height: 1.55;
        display: block;
    }
    .insight-card.info {
        background: var(--blue-pale);
        border-color: var(--blue);
    }
    .insight-card.info b  { color: #1E40AF; }
    .insight-card.info small { color: #3B82F6; }
    .insight-card.success {
        background: var(--green-pale);
        border-color: var(--green);
    }
    .insight-card.success b  { color: #065F46; }
    .insight-card.success small { color: #059669; }
    .insight-card.warn {
        background: var(--amber-pale);
        border-color: var(--amber);
    }
    .insight-card.warn b  { color: #92400E; }
    .insight-card.warn small { color: #B45309; }
    .insight-card.danger {
        background: var(--red-pale);
        border-color: var(--red);
    }
    .insight-card.danger b  { color: #991B1B; }
    .insight-card.danger small { color: #DC2626; }

    /* =====================================================
       RISK SCORE CARD
    ===================================================== */
    .risk-score-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 1.8rem 1.5rem;
        text-align: center;
        box-shadow: var(--shadow-sm);
    }
    .risk-score-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: var(--text-muted);
        margin-bottom: 0.5rem;
    }
    .risk-score-number {
        font-family: var(--font-mono);
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1;
        margin: 0.2rem 0 0.6rem;
    }
    .risk-score-number.low    { color: var(--green); }
    .risk-score-number.medium { color: var(--amber); }
    .risk-score-number.high   { color: var(--red);   }
    .risk-badge {
        display: inline-block;
        padding: 5px 16px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .risk-badge.low    { background:#D1FAE5; color:#065F46; }
    .risk-badge.medium { background:#FEF3C7; color:#92400E; }
    .risk-badge.high   { background:#FEE2E2; color:#991B1B; }
    .risk-score-sub {
        font-size: 0.75rem;
        color: var(--text-muted);
        margin-top: 0.7rem;
        line-height: 1.5;
    }

    /* =====================================================
       SIDEBAR REDESIGN
    ===================================================== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #0D1B38 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.06) !important;
    }
    [data-testid="stSidebar"] > div {
        padding-top: 1rem !important;
    }

    /* Sidebar logo area */
    [data-testid="stSidebar"] .stMarkdown h2 {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.3px;
    }

    /* All sidebar text */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {
        color: #CBD5E1 !important;
    }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
    }

    /* Sidebar section dividers */
    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.08) !important;
        margin: 1rem 0 !important;
    }

    /* Sidebar inputs */
    [data-testid="stSidebar"] .stNumberInput input,
    [data-testid="stSidebar"] .stTextInput input {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        color: #FFFFFF !important;
        border-radius: var(--radius-sm) !important;
    }
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        color: #FFFFFF !important;
        border-radius: var(--radius-sm) !important;
    }

    /* Slider track */
    [data-testid="stSidebar"] .stSlider [data-baseweb="slider"] div[role="slider"] {
        background: var(--blue) !important;
    }

    /* Sidebar group labels */
    .sidebar-group-label {
        font-size: 0.62rem;
        font-weight: 700;
        letter-spacing: 1.4px;
        text-transform: uppercase;
        color: #475569 !important;
        margin: 1.2rem 0 0.5rem;
        padding: 0 0.2rem;
        display: block;
    }

    /* =====================================================
       TABS — PREMIUM SEGMENTED CONTROL
    ===================================================== */
    .stTabs [data-baseweb="tab-list"] {
        background: #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 4px !important;
        gap: 3px !important;
        border: none !important;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 9px !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 0.84rem !important;
        color: var(--text-secondary) !important;
        padding: 0.45rem 1rem !important;
        transition: all 0.18s ease !important;
    }
    .stTabs [aria-selected="true"] {
        background: #FFFFFF !important;
        color: var(--text-primary) !important;
        box-shadow: 0 2px 8px rgba(15,23,42,0.1) !important;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 1.2rem !important;
    }

    /* =====================================================
       CHART CONTAINERS
    ===================================================== */
    .chart-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 0.5rem;
        box-shadow: var(--shadow-sm);
    }

    /* =====================================================
       DOWNLOAD BUTTONS
    ===================================================== */
    .stDownloadButton > button {
        background: var(--blue) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        padding: 0.6rem 1.4rem !important;
        width: 100% !important;
        transition: background 0.2s ease, transform 0.15s ease !important;
        box-shadow: 0 2px 8px rgba(37,99,235,0.3) !important;
    }
    .stDownloadButton > button:hover {
        background: #1D4ED8 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 14px rgba(37,99,235,0.4) !important;
    }

    /* =====================================================
       DATAFRAME / TABLE
    ===================================================== */
    .stDataFrame {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden;
    }
    .stDataFrame thead tr th {
        background: #F8FAFC !important;
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
        font-size: 0.78rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        border-bottom: 2px solid var(--border) !important;
        padding: 12px 16px !important;
    }
    .stDataFrame tbody tr td {
        font-family: var(--font-mono);
        font-size: 0.84rem !important;
        color: var(--text-primary) !important;
        padding: 10px 16px !important;
        border-bottom: 1px solid #F1F5F9 !important;
    }
    .stDataFrame tbody tr:hover td {
        background: #F8FAFC !important;
    }

    /* =====================================================
       SEARCH INPUT
    ===================================================== */
    .stTextInput input {
        border: 1.5px solid var(--border) !important;
        border-radius: 10px !important;
        font-size: 0.88rem !important;
        padding: 0.55rem 1rem !important;
        color: var(--text-primary) !important;
        background: var(--bg-card) !important;
        transition: border-color 0.18s ease !important;
    }
    .stTextInput input:focus {
        border-color: var(--blue) !important;
        box-shadow: 0 0 0 3px rgba(37,99,235,0.12) !important;
    }

    /* =====================================================
       REFI CARD
    ===================================================== */
    .refi-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 1.6rem 1.8rem;
        box-shadow: var(--shadow-sm);
        display: flex;
        flex-direction: column;
        min-height: 140px;
        position: relative;
        overflow: hidden;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .refi-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    .refi-card-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: var(--text-muted);
        margin-bottom: 0.5rem;
    }
    .refi-card-value {
        font-family: var(--font-mono);
        font-size: 1.8rem;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.1;
        margin-bottom: 0.4rem;
    }
    .refi-card-sub {
        font-size: 0.78rem;
        color: var(--text-muted);
        margin-top: auto;
    }
    .refi-card.red   { border-top: 3px solid var(--red); }
    .refi-card.blue  { border-top: 3px solid var(--blue); }
    .refi-card.green { border-top: 3px solid var(--green); }

    /* =====================================================
       FORECAST TABLE
    ===================================================== */
    .forecast-row {
        display: flex;
        align-items: center;
        padding: 0.75rem 1rem;
        border-radius: var(--radius-md);
        background: var(--bg-card);
        border: 1px solid var(--border);
        margin-bottom: 8px;
        gap: 1rem;
        box-shadow: var(--shadow-sm);
    }
    .forecast-milestone {
        font-weight: 700;
        font-size: 0.85rem;
        color: var(--text-primary);
        min-width: 130px;
    }
    .forecast-period {
        font-family: var(--font-mono);
        font-size: 0.82rem;
        color: var(--text-secondary);
        min-width: 100px;
    }
    .forecast-balance {
        font-family: var(--font-mono);
        font-size: 0.82rem;
        color: var(--text-secondary);
        min-width: 120px;
    }
    .forecast-interest {
        font-family: var(--font-mono);
        font-size: 0.82rem;
        color: var(--red);
        font-weight: 600;
        margin-left: auto;
    }
    .milestone-bar-wrap {
        flex: 1;
        height: 6px;
        background: #F1F5F9;
        border-radius: 3px;
        overflow: hidden;
    }
    .milestone-bar-fill {
        height: 100%;
        border-radius: 3px;
        background: linear-gradient(90deg, var(--blue), var(--cyan));
    }

    /* =====================================================
       FOOTER
    ===================================================== */
    .app-footer {
        text-align: center;
        padding: 2.5rem 1rem 1.5rem;
        color: var(--text-muted);
        font-size: 0.78rem;
        border-top: 1px solid var(--border);
        margin-top: 3rem;
        line-height: 1.8;
    }
    .app-footer strong { color: var(--text-secondary); }

    /* =====================================================
       METRIC CONTAINER OVERRIDE
    ===================================================== */
    div[data-testid="metric-container"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        padding: 1rem 1.2rem !important;
        box-shadow: var(--shadow-sm) !important;
    }

    /* =====================================================
       INFO BOXES
    ===================================================== */
    .stInfo {
        background: var(--blue-pale) !important;
        border: 1px solid rgba(37,99,235,0.2) !important;
        border-radius: var(--radius-md) !important;
        color: #1E40AF !important;
    }

    </style>
    """, unsafe_allow_html=True)


# ============================================================
# PLOTLY THEME — ENTERPRISE STANDARD
# ============================================================

CHART_THEME = dict(
    template="plotly_white",
    font=dict(family="Inter, system-ui, sans-serif", size=12, color="#334155"),
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF",
    margin=dict(l=10, r=10, t=44, b=10),
    hoverlabel=dict(
        bgcolor="#0F172A",
        font=dict(family="Inter", size=12, color="white"),
        bordercolor="#0F172A"
    ),
    xaxis=dict(
        showgrid=True,
        gridcolor="#F1F5F9",
        gridwidth=1,
        zeroline=False,
        tickfont=dict(size=11, color="#64748B"),
        linecolor="#E2E8F0"
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="#F1F5F9",
        gridwidth=1,
        zeroline=False,
        tickfont=dict(size=11, color="#64748B"),
        linecolor="#E2E8F0"
    ),
    legend=dict(
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#E2E8F0",
        borderwidth=1,
        font=dict(size=11, color="#475569"),
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0
    )
)

COLORS = {
    "blue":   "#2563EB",
    "cyan":   "#06B6D4",
    "green":  "#10B981",
    "amber":  "#F59E0B",
    "red":    "#EF4444",
    "purple": "#8B5CF6",
    "navy":   "#0F172A",
    "slate":  "#64748B",
}


# ============================================================
# CURRENCY & FORMAT UTILITIES
# ============================================================

CURRENCY_SYMBOLS = {
    "INR (₹)": "₹",
    "USD ($)": "$",
    "EUR (€)": "€",
    "GBP (£)": "£",
    "AED (د.إ)": "د.إ",
    "JPY (¥)": "¥",
    "SGD (S$)": "S$",
}

def fmt(value: float, sym: str, abbrev: bool = True) -> str:
    if abbrev:
        if abs(value) >= 1_00_00_000:
            return f"{sym}{value/1_00_00_000:.2f} Cr"
        elif abs(value) >= 1_00_000:
            return f"{sym}{value/1_00_000:.2f} L"
    return f"{sym}{value:,.2f}"

def fmt_plain(value: float, sym: str) -> str:
    return f"{sym}{value:,.2f}"


# ============================================================
# AMORTIZATION ENGINE
# ============================================================

def calculate_emi(principal: float, annual_rate: float, months: int) -> float:
    if annual_rate == 0:
        return principal / months if months > 0 else 0
    r = annual_rate / 100 / 12
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)


def build_schedule(
    loan_amount: float,
    annual_rate: float,
    loan_years: int,
    extra_payment: float = 0,
    frequency: str = "Monthly"
) -> pd.DataFrame:
    freq_map = {"Monthly": 12, "Quarterly": 4, "Annual": 1}
    ppy = freq_map[frequency]
    total_periods = loan_years * ppy
    period_rate = annual_rate / 100 / ppy

    if period_rate == 0:
        base_pmt = loan_amount / total_periods
    else:
        base_pmt = (
            loan_amount * period_rate * (1 + period_rate) ** total_periods
            / ((1 + period_rate) ** total_periods - 1)
        )

    extra_ppp = extra_payment * (12 / ppy)
    payment = base_pmt + extra_ppp

    rows = []
    balance = loan_amount
    cum_int = cum_prin = 0.0

    for period in range(1, total_periods + 1):
        interest = balance * period_rate
        principal = payment - interest
        if principal > balance:
            principal = balance
            payment = principal + interest
        balance -= principal
        cum_int   += interest
        cum_prin  += principal
        rows.append({
            "Period": period,
            "Payment": round(payment, 2),
            "Principal": round(principal, 2),
            "Interest": round(interest, 2),
            "Cumulative Interest": round(cum_int, 2),
            "Cumulative Principal": round(cum_prin, 2),
            "Remaining Balance": round(max(balance, 0), 2),
        })
        if balance <= 0:
            break

    return pd.DataFrame(rows)


# ============================================================
# RISK SCORING
# ============================================================

def compute_risk(loan_amount, annual_income, interest_rate, loan_years):
    if annual_income <= 0:
        return 20, "High"
    emi = calculate_emi(loan_amount, interest_rate, loan_years * 12)
    dti = (emi * 12) / annual_income
    score = 0
    score += 40 if dti < 0.30 else (25 if dti < 0.45 else 5)
    score += 30 if loan_years <= 10 else (20 if loan_years <= 20 else 10)
    score += 30 if interest_rate < 8 else (18 if interest_rate < 13 else 5)
    label = "Low" if score >= 70 else ("Medium" if score >= 42 else "High")
    return min(score, 100), label


# ============================================================
# MULTI-SCENARIO ENGINE
# ============================================================

def multi_scenario(loan_amount, base_rate, loan_years):
    rows = []
    for rate in [base_rate - 2, base_rate - 1, base_rate, base_rate + 1, base_rate + 2]:
        if rate <= 0:
            continue
        for tenure in [max(1, loan_years - 5), loan_years, loan_years + 5]:
            months = tenure * 12
            emi    = calculate_emi(loan_amount, rate, months)
            total  = emi * months
            intst  = total - loan_amount
            rows.append({
                "Rate (%)": round(rate, 1),
                "Tenure (Yrs)": tenure,
                "EMI": round(emi, 2),
                "Total Payment": round(total, 2),
                "Total Interest": round(intst, 2),
                "Interest %": round((intst / loan_amount) * 100, 1),
            })
    return pd.DataFrame(rows)


# ============================================================
# SIDEBAR
# ============================================================

def sidebar_inputs():
    sb = st.sidebar

    sb.markdown("""
    <div style="display:flex;align-items:center;gap:10px;padding:0.5rem 0 1rem;">
        <div style="width:36px;height:36px;background:linear-gradient(135deg,#2563EB,#06B6D4);
                    border-radius:10px;display:flex;align-items:center;justify-content:center;
                    font-size:1.1rem;">🏦</div>
        <div>
            <div style="color:#FFFFFF;font-weight:700;font-size:1rem;line-height:1.2;">LoanIQ</div>
            <div style="color:#475569;font-size:0.68rem;letter-spacing:0.8px;text-transform:uppercase;">
                Enterprise Platform
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    sb.markdown("---")

    sb.markdown('<span class="sidebar-group-label">Currency & Loan Type</span>', unsafe_allow_html=True)
    currency_key = sb.selectbox("Currency", list(CURRENCY_SYMBOLS.keys()), index=0, label_visibility="collapsed")
    currency = CURRENCY_SYMBOLS[currency_key]

    loan_type = sb.selectbox("Loan Type", [
        "🏠 Home / Mortgage", "🚗 Auto Loan", "💼 Business Loan",
        "👤 Personal Loan", "🎓 Education Loan", "📐 Custom"
    ], label_visibility="visible")

    defaults = {
        "🏠 Home / Mortgage":  (5_000_000,  8.5, 20),
        "🚗 Auto Loan":        (  800_000,   9.5,  5),
        "💼 Business Loan":    (2_000_000,  11.0,  7),
        "👤 Personal Loan":    (  300_000,  14.0,  3),
        "🎓 Education Loan":   (  500_000,  10.5,  5),
        "📐 Custom":           (1_000_000,  10.0, 10),
    }
    def_amt, def_rate, def_yrs = defaults[loan_type]

    sb.markdown("---")
    sb.markdown('<span class="sidebar-group-label">Loan Parameters</span>', unsafe_allow_html=True)

    loan_amount = sb.number_input(
        f"Loan Amount ({currency})", min_value=10_000,
        max_value=100_000_000, value=def_amt, step=10_000
    )
    interest_rate = sb.slider("Annual Interest Rate (%)", 1.0, 30.0, def_rate, 0.1)
    loan_years    = sb.slider("Tenure (Years)", 1, 40, def_yrs, 1)

    sb.markdown("---")
    sb.markdown('<span class="sidebar-group-label">Extra Payments</span>', unsafe_allow_html=True)

    extra_payment = sb.number_input(
        f"Extra Monthly Payment ({currency})", min_value=0, value=0, step=1000
    )
    frequency = sb.selectbox("Payment Frequency", ["Monthly", "Quarterly", "Annual"])

    sb.markdown("---")
    sb.markdown('<span class="sidebar-group-label">Risk & Refinancing</span>', unsafe_allow_html=True)

    annual_income = sb.number_input(
        f"Annual Income ({currency})", min_value=0, value=1_200_000, step=50_000
    )
    refi_rate = sb.number_input(
        "Refinance Rate (%)", min_value=1.0, max_value=30.0,
        value=max(1.0, round(interest_rate - 1.5, 1)), step=0.1
    )

    sb.markdown("---")
    sb.markdown(
        '<div style="color:#334155;font-size:0.72rem;text-align:center;padding:0.5rem 0;">'
        'LoanIQ v3.0 · Enterprise Edition<br>'
        '<span style="color:#1E40AF;">Bloomberg-grade Analytics</span></div>',
        unsafe_allow_html=True
    )

    return (loan_amount, interest_rate, loan_years, extra_payment,
            frequency, currency, annual_income, refi_rate, loan_type)


# ============================================================
# HEADER
# ============================================================

def render_header(loan_type, currency, loan_amount, base_emi, total_interest, total_payment, sym):
    overpay_pct = (total_interest / loan_amount) * 100 if loan_amount else 0
    st.markdown(f"""
    <div class="app-header">
        <div class="app-header-badge">⚡ Enterprise Edition &nbsp;·&nbsp; Real-time Analytics</div>
        <h1>LoanIQ — Financial Analytics Platform</h1>
        <p>{loan_type.split(' ', 1)[-1]} Analysis &nbsp;·&nbsp; Currency: {sym} &nbsp;·&nbsp;
           Powered by Python · Streamlit · Plotly</p>
        <div class="header-stats">
            <div class="header-stat-item">
                <span class="header-stat-label">Loan Amount</span>
                <span class="header-stat-value">{fmt(loan_amount, sym)}</span>
            </div>
            <div class="header-stat-item">
                <span class="header-stat-label">Monthly EMI</span>
                <span class="header-stat-value">{fmt_plain(base_emi, sym)}</span>
            </div>
            <div class="header-stat-item">
                <span class="header-stat-label">Total Interest</span>
                <span class="header-stat-value">{fmt(total_interest, sym)}</span>
            </div>
            <div class="header-stat-item">
                <span class="header-stat-label">Total Repayment</span>
                <span class="header-stat-value">{fmt(total_payment, sym)}</span>
            </div>
            <div class="header-stat-item">
                <span class="header-stat-label">Overpayment</span>
                <span class="header-stat-value">{overpay_pct:.1f}%</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# KPI ROW
# ============================================================

def kpi_card(label, value, sub, color, icon, sub_class=""):
    return f"""
    <div class="kpi-card kpi-{color}">
        <div class="kpi-card-top">
            <div><!-- spacer --></div>
            <div class="kpi-icon-wrap">{icon}</div>
        </div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub {sub_class}">{sub}</div>
    </div>
    """

def render_kpi_row(df, df_base, loan_amount, base_emi, interest_rate, loan_years, extra_payment, sym):
    total_interest  = df["Interest"].sum()
    total_payment   = df["Payment"].sum()
    actual_periods  = len(df)
    original_periods = loan_years * 12

    base_interest   = df_base["Interest"].sum()
    interest_saved  = base_interest - total_interest
    months_saved    = original_periods - actual_periods
    overpay_pct     = (total_interest / loan_amount) * 100

    sh("📋 Executive KPI Dashboard")

    row1_html = f"""
    <div class="kpi-grid">
        {kpi_card("Loan Amount",    fmt(loan_amount, sym),   f"{loan_years}-year tenure",          "blue",   "🏠")}
        {kpi_card("Monthly EMI",    fmt_plain(base_emi, sym), f"@ {interest_rate:.1f}% p.a.",      "cyan",   "📅")}
        {kpi_card("Total Interest", fmt(total_interest, sym), f"{overpay_pct:.1f}% of principal",  "amber",  "📈")}
        {kpi_card("Total Repayment",fmt(total_payment, sym),  f"over {actual_periods} periods",    "red",    "💳")}
        {kpi_card("Interest Saved", fmt(interest_saved, sym), f"↓ {months_saved} months early",   "green",  "💰",
                  "pos" if interest_saved > 0 else "")}
    </div>
    """
    st.markdown(row1_html, unsafe_allow_html=True)

    monthly_saving = interest_saved / max(actual_periods, 1)
    row2_html = f"""
    <div class="kpi-grid-4">
        {kpi_card("Payoff Duration",   f"{actual_periods} periods",  f"of {original_periods} originally planned",  "blue",   "⏱️")}
        {kpi_card("Interest Burden",   f"{overpay_pct:.1f}%",        "of principal paid as interest",               "amber",  "📊")}
        {kpi_card("Avg Period Saving", fmt(monthly_saving, sym),     "per period with extra payment",               "green",  "✅")}
        {kpi_card("Nominal Rate",      f"{interest_rate:.2f}%",      "effective annual interest rate",              "purple", "🎯")}
    </div>
    """
    st.markdown(row2_html, unsafe_allow_html=True)


# ============================================================
# SECTION HEADER HELPER
# ============================================================

def sh(title: str, icon: str = "📊", count: str = ""):
    count_html = f'<span class="section-header-count">{count}</span>' if count else ""
    st.markdown(f"""
    <div class="section-header">
        <div class="section-header-icon">{icon}</div>
        <span class="section-header-text">{title}</span>
        {count_html}
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CHART FUNCTIONS
# ============================================================

def apply_theme(fig, title="", height=320):
    fig.update_layout(**CHART_THEME, title=dict(text=title, font=dict(size=13, color="#0F172A", weight=600)), height=height)
    return fig

def chart_balance_decay(df, sym):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Remaining Balance"],
        mode="lines", fill="tozeroy",
        line=dict(color=COLORS["blue"], width=2.5),
        fillcolor="rgba(37,99,235,0.08)",
        name="Outstanding Balance",
        hovertemplate=f"<b>Period %{{x}}</b><br>Balance: {sym}%{{y:,.0f}}<extra></extra>"
    ))
    return apply_theme(fig, "Loan Balance Decay Curve", 320)

def chart_pi_trend(df, sym):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Principal"], mode="lines",
        name="Principal", line=dict(color=COLORS["green"], width=2),
        hovertemplate=f"Period %{{x}}<br>{sym}%{{y:,.0f}}<extra></extra>"
    ))
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Interest"], mode="lines",
        name="Interest", line=dict(color=COLORS["red"], width=2, dash="dash"),
        hovertemplate=f"Period %{{x}}<br>{sym}%{{y:,.0f}}<extra></extra>"
    ))
    return apply_theme(fig, "Principal vs Interest Per Period", 320)

def chart_cumulative(df, sym):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Cumulative Interest"],
        mode="lines", fill="tozeroy",
        line=dict(color=COLORS["amber"], width=2.5),
        fillcolor="rgba(245,158,11,0.10)",
        name="Cumulative Interest",
        hovertemplate=f"Period %{{x}}<br>{sym}%{{y:,.0f}}<extra></extra>"
    ))
    fig.add_trace(go.Scatter(
        x=df["Period"], y=df["Cumulative Principal"],
        mode="lines", line=dict(color=COLORS["blue"], width=2),
        name="Cumulative Principal",
        hovertemplate=f"Period %{{x}}<br>{sym}%{{y:,.0f}}<extra></extra>"
    ))
    return apply_theme(fig, "Cumulative Principal & Interest", 320)

def chart_donut(loan_amount, total_interest, sym):
    fig = go.Figure(go.Pie(
        labels=["Principal", "Total Interest"],
        values=[loan_amount, total_interest],
        hole=0.62,
        marker=dict(
            colors=[COLORS["blue"], COLORS["red"]],
            line=dict(color="white", width=3)
        ),
        textinfo="label+percent",
        textfont=dict(size=11),
        hovertemplate=f"<b>%{{label}}</b><br>{sym}%{{value:,.0f}}<extra></extra>"
    ))
    total = loan_amount + total_interest
    fig.add_annotation(
        text=f"<b>{sym}{total/1e5:.1f}L</b><br><span style='font-size:10px;color:#64748B'>Total</span>",
        x=0.5, y=0.5, showarrow=False,
        font=dict(size=14, color="#0F172A")
    )
    fig.update_layout(**{**CHART_THEME, "showlegend": True}, title=dict(text="Payment Distribution", font=dict(size=13, color="#0F172A")), height=320)
    return fig

def chart_annual_stack(df):
    df2 = df.copy()
    df2["Year"] = ((df2["Period"] - 1) // 12) + 1
    ann = df2.groupby("Year").agg({"Principal": "sum", "Interest": "sum"}).reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=ann["Year"], y=ann["Principal"], name="Principal",
                         marker_color=COLORS["blue"], marker_line_width=0))
    fig.add_trace(go.Bar(x=ann["Year"], y=ann["Interest"],  name="Interest",
                         marker_color=COLORS["amber"], marker_line_width=0))
    fig.update_layout(**CHART_THEME, barmode="stack", title=dict(text="Annual Payment Breakdown", font=dict(size=13, color="#0F172A")), height=320)
    return fig

def chart_extra_impact(df_base, df_extra, sym):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_base["Period"], y=df_base["Remaining Balance"],
        mode="lines", name="Without Extra Payments",
        line=dict(color=COLORS["red"], width=2, dash="dot"),
    ))
    fig.add_trace(go.Scatter(
        x=df_extra["Period"], y=df_extra["Remaining Balance"],
        mode="lines", name="With Extra Payments",
        line=dict(color=COLORS["green"], width=2.5),
        fill="tonexty", fillcolor="rgba(16,185,129,0.07)"
    ))
    return apply_theme(fig, "Extra Payment Impact on Payoff", 320)

def chart_heatmap(df_scen):
    pivot = df_scen.pivot(index="Tenure (Yrs)", columns="Rate (%)", values="Total Interest")
    text_vals = [[f"{v/1e5:.1f}L" if v >= 1e5 else f"{v:,.0f}" for v in row] for row in pivot.values]
    fig = go.Figure(go.Heatmap(
        z=pivot.values,
        x=[f"{c}%" for c in pivot.columns],
        y=[f"{r} Yr" for r in pivot.index],
        colorscale=[[0, "#D1FAE5"], [0.4, "#FEF3C7"], [1, "#FEE2E2"]],
        text=text_vals, texttemplate="%{text}",
        showscale=True,
        colorbar=dict(thickness=12, len=0.8, tickfont=dict(size=10)),
        hovertemplate="Rate: %{x}<br>Tenure: %{y}<br>Interest: %{text}<extra></extra>"
    ))
    fig.update_layout(**CHART_THEME, title=dict(text="Interest Cost Heatmap (Rate × Tenure)", font=dict(size=13)), height=340)
    return fig

def chart_refi(df_current, df_refi, sym):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_current["Period"], y=df_current["Remaining Balance"],
        mode="lines", name="Current Rate",
        line=dict(color=COLORS["red"], width=2, dash="dot")
    ))
    fig.add_trace(go.Scatter(
        x=df_refi["Period"], y=df_refi["Remaining Balance"],
        mode="lines", name="Refinance Rate",
        line=dict(color=COLORS["green"], width=2.5)
    ))
    return apply_theme(fig, "Refinancing Impact — Balance Comparison", 320)

def chart_emi_by_rate(df_scen, loan_years, sym):
    sub = df_scen[df_scen["Tenure (Yrs)"] == loan_years].copy()
    if sub.empty:
        sub = df_scen.copy()
    fig = go.Figure(go.Bar(
        x=sub["Rate (%)"].astype(str).apply(lambda x: f"{x}%"),
        y=sub["EMI"],
        marker=dict(
            color=sub["EMI"],
            colorscale=[[0,"#D1FAE5"],[0.5,"#FEF3C7"],[1,"#FEE2E2"]],
            showscale=False,
            line=dict(width=0)
        ),
        text=sub["EMI"].apply(lambda x: f"{sym}{x:,.0f}"),
        textposition="outside",
        hovertemplate="Rate: %{x}<br>EMI: %{text}<extra></extra>"
    ))
    return apply_theme(fig, "EMI vs Interest Rate (Current Tenure)", 300)


# ============================================================
# INSIGHTS
# ============================================================

def render_insights(df, loan_amount, annual_income, interest_rate, loan_years, sym, extra_payment):
    total_interest = df["Interest"].sum()
    emi = df["Payment"].iloc[0]
    overpay_pct = (total_interest / loan_amount) * 100

    risk_score, risk_label = compute_risk(loan_amount, annual_income, interest_rate, loan_years)

    sh("AI-Powered Financial Insights", "🧠")

    col1, col2 = st.columns([2.2, 1])

    with col1:
        if annual_income > 0:
            dti = (emi * 12) / annual_income * 100
            dti_cls = "success" if dti < 30 else ("warn" if dti < 50 else "danger")
            dti_status = "Healthy ✓" if dti < 30 else ("Manageable" if dti < 50 else "Stressed ⚠️")
            st.markdown(f"""
            <div class="insight-card {dti_cls}">
                <b>📊 Debt-to-Income Ratio: {dti:.1f}% — {dti_status}</b>
                <small>Annual loan payments of {sym}{emi*12:,.0f} against income of {sym}{annual_income:,.0f}.
                Lenders prefer DTI below 35% for loan approval.</small>
            </div>""", unsafe_allow_html=True)

        burden_cls = "success" if overpay_pct < 40 else ("warn" if overpay_pct < 70 else "danger")
        st.markdown(f"""
        <div class="insight-card {burden_cls}">
            <b>💸 Interest Burden: {overpay_pct:.1f}% of Principal</b>
            <small>You pay {sym}{total_interest:,.0f} in interest on a {sym}{loan_amount:,.0f} loan.
            {"Low burden — excellent financial position." if overpay_pct < 40 else "Consider prepayments to significantly reduce interest cost."}</small>
        </div>""", unsafe_allow_html=True)

        # Smart suggestion
        suggested_extra = loan_amount * 0.005
        rec_df = build_schedule(loan_amount, interest_rate, loan_years, suggested_extra)
        rec_saved = total_interest - rec_df["Interest"].sum()
        if rec_saved > 0 and extra_payment == 0:
            months_gain = loan_years * 12 - len(rec_df)
            st.markdown(f"""
            <div class="insight-card success">
                <b>⚡ Smart Suggestion: Pay {sym}{suggested_extra:,.0f}/month extra</b>
                <small>Adding just 0.5% of principal monthly saves {sym}{rec_saved:,.0f} in interest
                and eliminates {months_gain} months from your loan tenure.</small>
            </div>""", unsafe_allow_html=True)

        # Rate alert
        if interest_rate > 12:
            st.markdown(f"""
            <div class="insight-card danger">
                <b>🔔 High Interest Rate Alert: {interest_rate:.1f}%</b>
                <small>Your rate is above 12%. Consider refinancing or negotiating with your lender.
                Even a 1% reduction could save {sym}{total_interest * 0.08:,.0f} over the loan tenure.</small>
            </div>""", unsafe_allow_html=True)

    with col2:
        risk_cls = risk_label.lower()
        st.markdown(f"""
        <div class="risk-score-card">
            <div class="risk-score-label">Financial Risk Score</div>
            <div class="risk-score-number {risk_cls}">{risk_score}</div>
            <div><span class="risk-badge {risk_cls}">{risk_label} Risk</span></div>
            <div class="risk-score-sub">
                Based on Debt-to-Income ratio,
                loan tenure, and interest rate.
                <br><br>
                <strong>Score components:</strong><br>
                DTI · Tenure · Rate
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# SCHEDULE TABLE
# ============================================================

def render_schedule_table(df, sym):
    sh("Detailed Amortization Schedule", "📋", f"{len(df)} periods")

    search = st.text_input("🔍 Filter by period number", "", placeholder="e.g. 12")
    disp = df.copy()
    if search:
        try:
            disp = disp[disp["Period"] == int(search)]
        except ValueError:
            pass

    for col in ["Payment","Principal","Interest","Cumulative Interest","Cumulative Principal","Remaining Balance"]:
        disp[col] = disp[col].apply(lambda x: f"{sym}{x:,.2f}")

    st.dataframe(disp, use_container_width=True, height=420)


# ============================================================
# EXPORT
# ============================================================

def export_csv(df):
    return df.to_csv(index=False).encode("utf-8")

def export_excel(df, loan_amount, base_emi, interest_rate, loan_years):
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        pd.DataFrame({
            "Parameter": ["Loan Amount","Interest Rate (%)","Tenure (Years)","Monthly EMI",
                          "Total Interest","Total Payment","Interest %"],
            "Value": [loan_amount, f"{interest_rate}%", loan_years, round(base_emi, 2),
                      round(df["Interest"].sum(), 2), round(df["Payment"].sum(), 2),
                      f"{(df['Interest'].sum()/loan_amount)*100:.2f}%"]
        }).to_excel(writer, sheet_name="Executive Summary", index=False)
        df.to_excel(writer, sheet_name="Amortization Schedule", index=False)
    return buf.getvalue()


# ============================================================
# MAIN
# ============================================================

def main():
    load_css()

    (loan_amount, interest_rate, loan_years, extra_payment,
     frequency, sym, annual_income, refi_rate, loan_type) = sidebar_inputs()

    months   = loan_years * 12
    base_emi = calculate_emi(loan_amount, interest_rate, months)

    df      = build_schedule(loan_amount, interest_rate, loan_years, extra_payment, frequency)
    df_base = build_schedule(loan_amount, interest_rate, loan_years, 0, frequency)
    df_refi = build_schedule(loan_amount, refi_rate, loan_years, extra_payment, frequency)

    total_interest = df["Interest"].sum()
    total_payment  = df["Payment"].sum()

    render_header(loan_type, sym, loan_amount, base_emi, total_interest, total_payment, sym)
    render_kpi_row(df, df_base, loan_amount, base_emi, interest_rate, loan_years, extra_payment, sym)

    # ---- TABS ----
    tabs = st.tabs([
        "📊 Dashboard",
        "📈 Analytics",
        "🔀 Scenarios",
        "🔄 Refinancing",
        "📋 Schedule",
        "🧠 Insights",
        "⬇️ Export",
    ])

    # ----- TAB 1: DASHBOARD -----
    with tabs[0]:
        sh("Executive Dashboard", "📊")
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(chart_balance_decay(df, sym), use_container_width=True)
        with c2:
            st.plotly_chart(chart_donut(loan_amount, total_interest, sym), use_container_width=True)

        c3, c4 = st.columns(2)
        with c3:
            st.plotly_chart(chart_pi_trend(df, sym), use_container_width=True)
        with c4:
            st.plotly_chart(chart_annual_stack(df), use_container_width=True)

    # ----- TAB 2: ANALYTICS -----
    with tabs[1]:
        sh("Advanced Financial Analytics", "📈")
        st.plotly_chart(chart_cumulative(df, sym), use_container_width=True)

        if extra_payment > 0:
            st.plotly_chart(chart_extra_impact(df_base, df, sym), use_container_width=True)
        else:
            st.info("💡 Set an extra monthly payment in the sidebar to see prepayment impact analysis.")

        sh("Payoff Milestone Forecast", "📅")
        milestones = [0.25, 0.50, 0.75, 1.0]
        for pct in milestones:
            target = loan_amount * (1 - pct)
            rows = df[df["Remaining Balance"] <= target]
            period = int(rows["Period"].iloc[0]) if len(rows) > 0 else len(df)
            interest_so_far = df[df["Period"] <= period]["Interest"].sum()
            bar_width = int(pct * 100)
            label = f"{int(pct*100)}% Paid Off"
            rem = max(0, loan_amount * (1 - pct))
            st.markdown(f"""
            <div class="forecast-row">
                <span class="forecast-milestone">{label}</span>
                <span class="forecast-period">Period {period}</span>
                <div class="milestone-bar-wrap">
                    <div class="milestone-bar-fill" style="width:{bar_width}%"></div>
                </div>
                <span class="forecast-balance">{sym}{rem:,.0f} left</span>
                <span class="forecast-interest">{sym}{interest_so_far:,.0f} paid</span>
            </div>
            """, unsafe_allow_html=True)

    # ----- TAB 3: SCENARIOS -----
    with tabs[2]:
        sh("Multi-Scenario Comparison", "🔀")
        df_scen = multi_scenario(loan_amount, interest_rate, loan_years)

        styled = df_scen.copy()
        styled["EMI"]           = styled["EMI"].apply(lambda x: f"{sym}{x:,.2f}")
        styled["Total Payment"] = styled["Total Payment"].apply(lambda x: f"{sym}{x:,.2f}")
        styled["Total Interest"]= styled["Total Interest"].apply(lambda x: f"{sym}{x:,.2f}")
        styled["Interest %"]    = styled["Interest %"].apply(lambda x: f"{x}%")
        st.dataframe(styled, use_container_width=True)

        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(chart_heatmap(df_scen), use_container_width=True)
        with c2:
            st.plotly_chart(chart_emi_by_rate(df_scen, loan_years, sym), use_container_width=True)

    # ----- TAB 4: REFINANCING -----
    with tabs[3]:
        sh("Refinancing Calculator", "🔄")

        curr_int = total_interest
        refi_int = df_refi["Interest"].sum()
        refi_sav = curr_int - refi_int
        refi_emi = df_refi["Payment"].iloc[0]

        c1, c2, c3 = st.columns(3)
        for col, (label, value, sub, clr) in zip(
            [c1, c2, c3],
            [
                ("Current Rate Cost",   fmt(curr_int, sym), f"@ {interest_rate:.1f}% p.a.", "red"),
                ("Refinance Rate Cost", fmt(refi_int, sym), f"@ {refi_rate:.1f}% p.a.",    "blue"),
                ("Total Savings",       fmt(refi_sav, sym), "✅ Refinancing recommended" if refi_sav > 0 else "⚠️ Current rate is better", "green"),
            ]
        ):
            with col:
                st.markdown(f"""
                <div class="refi-card {clr}">
                    <div class="refi-card-label">{label}</div>
                    <div class="refi-card-value">{value}</div>
                    <div class="refi-card-sub">{sub}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.plotly_chart(chart_refi(df, df_refi, sym), use_container_width=True)

        # Comparison table
        sh("Refinancing Summary", "📋")
        comp_df = pd.DataFrame({
            "Metric": ["Interest Rate", "Monthly EMI", "Total Interest", "Total Payment", "Loan Periods"],
            "Current Loan": [f"{interest_rate:.1f}%", f"{sym}{base_emi:,.2f}",
                             f"{sym}{curr_int:,.2f}", f"{sym}{total_payment:,.2f}", len(df)],
            "After Refinancing": [f"{refi_rate:.1f}%", f"{sym}{refi_emi:,.2f}",
                                  f"{sym}{refi_int:,.2f}", f"{sym}{df_refi['Payment'].sum():,.2f}", len(df_refi)],
        })
        st.dataframe(comp_df, use_container_width=True)

    # ----- TAB 5: SCHEDULE -----
    with tabs[4]:
        render_schedule_table(df, sym)

    # ----- TAB 6: INSIGHTS -----
    with tabs[5]:
        render_insights(df, loan_amount, annual_income, interest_rate, loan_years, sym, extra_payment)

    # ----- TAB 7: EXPORT -----
    with tabs[6]:
        sh("Export & Download", "⬇️")
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📄 CSV Export")
            st.markdown("Full amortization schedule as a flat CSV file, ready for Excel or BI tools.")
            st.download_button(
                "⬇️ Download CSV",
                data=export_csv(df),
                file_name="amortization_schedule.csv",
                mime="text/csv",
                use_container_width=True
            )
        with c2:
            st.markdown("#### 📊 Excel Workbook")
            st.markdown("Multi-sheet Excel workbook with Executive Summary + full schedule.")
            st.download_button(
                "⬇️ Download Excel (.xlsx)",
                data=export_excel(df, loan_amount, base_emi, interest_rate, loan_years),
                file_name="loaniq_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

        sh("Data Preview", "📋", f"{len(df)} rows")
        st.dataframe(df.head(30), use_container_width=True)

    # ----- FOOTER -----
    st.markdown("""
    <div class="app-footer">
        <strong>LoanIQ</strong> — Enterprise Loan Amortization & Financial Analytics Platform<br>
        Built with Python · Streamlit · Plotly · Pandas · NumPy · OpenPyXL<br>
        <span>v3.0 · Bloomberg-grade UI · EPM-class Analytics</span>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
