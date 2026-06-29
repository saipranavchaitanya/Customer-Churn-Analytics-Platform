import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text
from db import engine
from components.styles import load_css
from components.kpi_cards import show_kpis

st.set_page_config(
    page_title="Customer Churn Analytics Platform",
    page_icon="📊",
    layout="wide"
)

load_css()

# -----------------------------
# Load Data
# -----------------------------
query = "SELECT * FROM customers;"
df = pd.read_sql(text(query), engine)

st.title("📊 Customer Churn Analytics Platform")

show_kpis(df)

st.markdown("---")

# -----------------------------
# KPIs
# -----------------------------

# -----------------------------
# Header
# -----------------------------
st.title("📊 Customer Churn Analytics Platform")

# -----------------------------
# KPI Cards
# -----------------------------


# -----------------------------
# Charts
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Status")

    fig = px.pie(
        df,
        names="customer_status",
        hole=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Contract Type")

    fig = px.bar(
        df["contract_type"].value_counts().reset_index(),
        x="contract_type",
        y="count"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Second Row
# -----------------------------
col3, col4 = st.columns(2)

with col3:

    st.subheader("Internet Service")

    fig = px.bar(
        df["internet_service"].value_counts().reset_index(),
        x="internet_service",
        y="count",
        color="internet_service"
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    st.subheader("State Wise Customers")

    fig = px.bar(
        df.groupby("state").size().reset_index(name="Customers"),
        x="state",
        y="Customers",
        color="Customers"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Customer Table
# -----------------------------
st.markdown("---")

st.subheader("Customer Data")

st.dataframe(df, use_container_width=True)