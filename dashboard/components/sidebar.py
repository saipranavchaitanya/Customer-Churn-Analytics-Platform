import streamlit as st

def sidebar_header():

    with st.sidebar:

        st.title("📊 Customer Analytics")
        st.caption("Business Intelligence Platform")

        st.divider()

        st.success("🟢 Database Connected")

        st.caption("Version 2.0")