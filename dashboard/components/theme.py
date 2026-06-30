import streamlit as st
from pathlib import Path

def load_theme():

    css = Path("assets/liquid_glass.css").read_text()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )