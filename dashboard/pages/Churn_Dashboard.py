import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text
from db import engine

st.set_page_config(
    page_title="Churn Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Churn Dashboard")

query = "SELECT * FROM customers"
df = pd.read_sql(text(query), engine)

# KPI
total = len(df)
churn = len(df[df["customer_status"] == "Churned"])
active = len(df[df["customer_status"] == "Active"])
rate = round((churn / total) * 100, 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers", total)
col2.metric("Active", active)
col3.metric("Churned", churn)
col4.metric("Churn Rate", f"{rate}%")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    fig = px.pie(
        df,
        names="customer_status",
        title="Customer Status",
        hole=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    contract = (
        df.groupby(["contract_type", "customer_status"])
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        contract,
        x="contract_type",
        y="Customers",
        color="customer_status",
        barmode="group",
        title="Contract Type vs Churn"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:

    internet = (
        df.groupby(["internet_service", "customer_status"])
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        internet,
        x="internet_service",
        y="Customers",
        color="customer_status",
        title="Internet Service"
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    state = (
        df.groupby("state")
        .size()
        .reset_index(name="Customers")
        .sort_values("Customers", ascending=False)
        .head(10)
    )

    fig = px.bar(
        state,
        x="Customers",
        y="state",
        orientation="h",
        title="Top 10 States"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Churn Data")

st.dataframe(df[df["customer_status"] == "Churned"], use_container_width=True)