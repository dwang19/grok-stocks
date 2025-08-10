import streamlit as st

def show_home_page():
    st.title("Welcome to Grok Stocks")
    st.write("Your position trading app. Click Start to begin.")
    if st.button("Start"):
        st.session_state.page = "macro_dashboard"  # Switch to dashboard on click