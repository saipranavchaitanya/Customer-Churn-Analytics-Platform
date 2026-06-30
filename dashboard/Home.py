import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text
from io import BytesIO

from db import engine
from components.styles import load_css
from components.kpi_cards import show_kpis
from components.chart_theme import apply_glass_chart
from components.sidebar import sidebar_header

# ---------------------------------------------------
# PAGE CONFIG (Must be the first Streamlit command)
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD CSS & SIDEBAR
# ---------------------------------------------------
load_css()
sidebar_header()

# ---------------------------------------------------
# HELPER FUNCTION
# ---------------------------------------------------
def to_excel(dataframe):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        dataframe.to_excel(writer, index=False)

    return output.getvalue()

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
query = "SELECT * FROM customers;"
df = pd.read_sql(text(query), engine)

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------
st.markdown("""
<div class="glass-card">
<h2>🎯 Dashboard Filters</h2>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    state = st.selectbox(
        "State",
        ["All"] + sorted(df["state"].dropna().unique().tolist())
    )

with c2:
    contract = st.selectbox(
        "Contract Type",
        ["All"] + sorted(df["contract_type"].dropna().unique().tolist())
    )

with c3:
    internet = st.selectbox(
        "Internet Service",
        ["All"] + sorted(df["internet_service"].dropna().unique().tolist())
    )

if state != "All":
    df = df[df["state"] == state]

if contract != "All":
    df = df[df["contract_type"] == contract]

if internet != "All":
    df = df[df["internet_service"] == internet]
    # ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("""
<div class="glass-card">

<h1 style="text-align:center;">
📊 Customer Churn Analytics Platform
</h1>

<p style="text-align:center;
color:#d6d6d6;
font-size:18px;">

Business Intelligence Dashboard

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------
show_kpis(df)

st.write("")

# ---------------------------------------------------
# CHARTS ROW 1
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.subheader("👥 Customer Status")

    fig = px.pie(
        df,
        names="customer_status",
        hole=0.60
    )

    fig = apply_glass_chart(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("📄 Contract Type")

    contract_df = (
    df["contract_type"]
    .value_counts()
    .rename_axis("contract_type")
    .reset_index(name="count")
)

    fig = px.bar(
        contract_df,
        x="contract_type",
        y="count",
        color="contract_type"
    )

    fig = apply_glass_chart(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ---------------------------------------------------
# CHARTS ROW 2
# ---------------------------------------------------
col3, col4 = st.columns(2)

with col3:

    st.subheader("🌐 Internet Service")

    internet_df = (
    df["internet_service"]
    .value_counts()
    .rename_axis("internet_service")
    .reset_index(name="count")
)

    fig = px.bar(
        internet_df,
        x="internet_service",
        y="count",
        color="internet_service"
    )

    fig = apply_glass_chart(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col4:

    st.subheader("📍 State Wise Customers")

    state_df = (
        df.groupby("state")
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        state_df,
        x="state",
        y="Customers",
        color="Customers"
    )

    fig = apply_glass_chart(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------------------
# CUSTOMER TABLE
# ---------------------------------------------------
st.write("")

st.markdown("""
<div class="table-title">
📋 Customer Database
</div>
""", unsafe_allow_html=True)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)

# ---------------------------------------------------
# EXPORT DATA
# ---------------------------------------------------
st.write("")

st.markdown("""
<div class="glass-card">
<h2>📥 Export Dashboard Data</h2>
</div>
""", unsafe_allow_html=True)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📄 Download Customer Data (CSV)",
    data=csv,
    file_name="customer_data.csv",
    mime="text/csv"
)

excel = to_excel(df)

st.download_button(
    label="📊 Download Customer Data (Excel)",
    data=excel,
    file_name="customer_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)