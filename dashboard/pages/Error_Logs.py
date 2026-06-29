import streamlit as st
import pandas as pd
from sqlalchemy import text
from db import engine

st.set_page_config(
    page_title="Error Logs",
    page_icon="❌",
    layout="wide"
)

st.title("❌ Error Logs")

query = """
SELECT *
FROM validation_errors
ORDER BY error_id DESC
"""

df = pd.read_sql(text(query), engine)

if df.empty:
    st.success("🎉 No Validation Errors Found")
else:
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "📥 Download Errors",
        df.to_csv(index=False),
        "validation_errors.csv",
        "text/csv"
    )