import streamlit as st
from pathlib import Path

def load_css():

    css_files = [
        "assets/styles.css",
        "assets/liquid_glass.css"
    ]

    all_css = ""

    for css_file in css_files:

        path = Path(css_file)

        if path.exists():

            all_css += path.read_text(encoding="utf-8")

    st.markdown(
        f"<style>{all_css}</style>",
        unsafe_allow_html=True
    )