import streamlit as st
from pathlib import Path

def load_css():

    css_path = Path("assets/liquid_glass.css")

    if css_path.exists():

        css = css_path.read_text(encoding="utf-8")

        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True
        )