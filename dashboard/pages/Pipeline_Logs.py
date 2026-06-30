import streamlit as st
import pandas as pd
from sqlalchemy import text
from components.sidebar import sidebar_header
from db import engine
from components.styles import load_css
st.set_page_config(
    page_title="Pipeline Logs",
    page_icon="📄",
    layout="wide"
)

load_css()



sidebar_header()


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