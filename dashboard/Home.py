import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text
from components.theme import load_theme
from db import engine
from io import BytesIO
from components.styles import load_css
from components.kpi_cards import show_kpis
from components.chart_theme import apply_glass_chart
from components.styles import load_css
from components.theme import load_liquid_glass
from components.chart_theme import apply_glass_chart
from components.theme_toggle import theme_toggle

load_css()
load_theme()
load_liquid_glass()
theme = theme_toggle()
if theme == "Light":

    st.markdown("""
    <script>

    document.body.classList.add("light-theme");

    </script>
    """, unsafe_allow_html=True)
def to_excel(dataframe):

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        dataframe.to_excel(writer, index=False)

    return output.getvalue()
# Utility: apply a consistent 'glass' style to Plotly figures
def apply_glass_chart(fig):
    try:
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(bgcolor="rgba(0,0,0,0)")
        )
    except Exception:
        pass
    return fig

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

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
query = "SELECT * FROM customers;"
df = pd.read_sql(text(query), engine)
# ---------------------------------------------------
# Filters
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
        ["All"] + sorted(df["state"].unique().tolist())
    )

with c2:
    contract = st.selectbox(
        "Contract Type",
        ["All"] + sorted(df["contract_type"].unique().tolist())
    )

with c3:
    internet = st.selectbox(
        "Internet Service",
        ["All"] + sorted(df["internet_service"].unique().tolist())
    )
    # Apply Filters

if state != "All":
    df = df[df["state"] == state]

if contract != "All":
    df = df[df["contract_type"] == contract]

if internet != "All":
    df = df[df["internet_service"] == internet]
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

    fig = apply_glass_chart(fig)

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

    fig = apply_glass_chart(fig)

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
# Export Data
# ---------------------------------------------------

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
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text

from db import engine
from components.styles import load_css
from components.kpi_cards import show_kpis
from components.chart_theme import apply_glass_chart
# ---------------------------------------------------
# Page Config (must be first)
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Load Theme
# ---------------------------------------------------
load_css()

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

<h1 style="text-align:center;">
📊 Customer Churn Analytics Platform
</h1>

<p style="text-align:center;color:#d6d6d6;font-size:18px;">
Business Intelligence Dashboard
</p>

</div>
""", unsafe_allow_html=True)

show_kpis(df)

st.write("")