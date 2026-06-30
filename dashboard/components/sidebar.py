import streamlit as st

def sidebar_header():

    with st.sidebar:

        st.markdown("""

        <div style="

        background:rgba(255,255,255,.08);

        backdrop-filter:blur(25px);

        border-radius:25px;

        padding:20px;

        text-align:center;

        margin-bottom:20px;

        ">

        <div style="font-size:55px;">
        📊
        </div>

        <h2 style="margin-bottom:5px;">
        Customer Analytics
        </h2>

        <p style="color:#D6D6D6;">
        Business Intelligence Platform
        </p>

        </div>

        """, unsafe_allow_html=True)

        st.success("🟢 Database Connected")

        st.caption("Version 2.0")