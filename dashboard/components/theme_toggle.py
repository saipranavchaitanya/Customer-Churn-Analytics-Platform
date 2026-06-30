import streamlit as st

def theme_toggle():

    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"

    with st.sidebar:

        st.markdown("### 🎨 Theme")

        if st.toggle("Light Mode"):

            st.session_state.theme = "Light"

        else:

            st.session_state.theme = "Dark"

    return st.session_state.theme