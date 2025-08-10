import streamlit as st
from view.home import show_home_page
from view.macro_dashboard import show_macro_dashboard

def run_app(api_key):
    # Initialize page state if not set (best practice: Default to Home)
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Show page based on state
    if st.session_state.page == "home":
        show_home_page()
    elif st.session_state.page == "macro_dashboard":
        show_macro_dashboard()