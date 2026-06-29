import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text
from db import engine

st.set_page_config(
    page_title="ETL Monitor",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ ETL Monitor")

query = """
SELECT *
FROM etl_logs
ORDER BY run_date DESC
"""

df = pd.read_sql(text(query), engine)

if df.empty:
    st.warning("No ETL Logs Found")
    st.stop()

latest = df.iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Pipeline", latest["pipeline_name"])
col2.metric("Status", latest["status"])
col3.metric("Records Loaded", latest["records_loaded"])
col4.metric("Execution Time", f"{latest['execution_time_seconds']} sec")

st.markdown("---")

fig = px.line(
    df,
    x="run_date",
    y="records_loaded",
    markers=True,
    title="Records Loaded History"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    df,
    x="run_date",
    y="execution_time_seconds",
    title="Execution Time History"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("ETL Log History")

st.dataframe(df, use_container_width=True)