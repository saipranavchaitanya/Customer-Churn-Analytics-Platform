import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main{
        background-color:#f8f9fa;
    }

    div[data-testid="metric-container"]{
        background:white;
        padding:18px;
        border-radius:15px;
        box-shadow:0px 3px 10px rgba(0,0,0,.12);
        text-align:center;
    }

    h1{
        color:#0F62FE;
    }

    </style>
    """,
    unsafe_allow_html=True)