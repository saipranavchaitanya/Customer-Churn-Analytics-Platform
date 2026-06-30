import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text
from pathlib import Path

from db import engine
from components.styles import load_css
from components.kpi_cards import show_kpis

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Load CSS
# ---------------------------------------------------
load_css()

css = Path("assets/liquid_glass.css").read_text()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
query = "SELECT * FROM customers;"
df = pd.read_sql(text(query), engine)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown("""
<div class="glass-card">
<h1 style="text-align:center;margin-bottom:0;">
📊 Customer Churn Analytics Platform
</h1>

<p style="text-align:center;
color:#cfd8dc;
font-size:18px;
margin-top:5px;">
Business Intelligence Dashboard
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------
show_kpis(df)

st.write("")

# ---------------------------------------------------
# Charts Row 1
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("👥 Customer Status")

    fig = px.pie(
        df,
        names="customer_status",
        hole=0.60
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("📄 Contract Type")

    fig = px.bar(
        df["contract_type"].value_counts().reset_index(),
        x="contract_type",
        y="count"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# Charts Row 2
# ---------------------------------------------------
col3, col4 = st.columns(2)

with col3:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("🌐 Internet Service")

    fig = px.bar(
        df["internet_service"].value_counts().reset_index(),
        x="internet_service",
        y="count",
        color="internet_service"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col4:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("📍 State Wise Customers")

    fig = px.bar(
        df.groupby("state").size().reset_index(name="Customers"),
        x="state",
        y="Customers",
        color="Customers"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# Customer Table
# ---------------------------------------------------
st.write("")

st.markdown("""
<div class="glass-card">
<h2>📋 Customer Data</h2>
</div>
""", unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)