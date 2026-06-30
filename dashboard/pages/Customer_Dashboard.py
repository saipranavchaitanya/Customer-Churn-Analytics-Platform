import streamlit as st
import pandas as pd
from sqlalchemy import text
from components.sidebar import sidebar_header
from db import engine
from components.styles import load_css
st.set_page_config(
    page_title="Customer Dashboard",
    page_icon="👥",
    layout="wide"
)

load_css()

sidebar_header()


st.title("👥 Customer Dashboard")

query = "SELECT * FROM customers"

df = pd.read_sql(text(query), engine)

st.sidebar.header("Filters")

state = st.sidebar.selectbox(
    "State",
    ["All"] + sorted(df["state"].unique().tolist())
)

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(df["gender"].unique().tolist())
)

contract = st.sidebar.selectbox(
    "Contract",
    ["All"] + sorted(df["contract_type"].unique().tolist())
)

if state != "All":
    df = df[df["state"] == state]

if gender != "All":
    df = df[df["gender"] == gender]

if contract != "All":
    df = df[df["contract_type"] == contract]

search = st.text_input("🔍 Search Customer Name")

if search:
    df = df[df["full_name"].str.contains(search, case=False)]

st.subheader("Customer Records")

st.dataframe(df, use_container_width=True)

st.download_button(
    "📥 Download CSV",
    df.to_csv(index=False),
    "customers.csv",
    "text/csv"
)