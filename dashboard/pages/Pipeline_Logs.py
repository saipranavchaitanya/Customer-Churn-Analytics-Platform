import streamlit as st
import pandas as pd
from sqlalchemy import text
from dashboard.components.sidebar import show_sidebar, sidebar_header
from db import engine
from components.styles import load_css
from components.theme import load_liquid_glass, load_theme

load_css()
load_theme()
show_sidebar()
load_liquid_glass()
sidebar_header()
st.set_page_config(
    page_title="Pipeline Logs",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Pipeline Logs")

query = """
SELECT *
FROM etl_logs
ORDER BY run_date DESC
"""

df = pd.read_sql(text(query), engine)

st.dataframe(df, use_container_width=True)

st.download_button(
    "📥 Download Logs",
    df.to_csv(index=False),
    "etl_logs.csv",
    "text/csv"
)