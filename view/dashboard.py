import streamlit as st
from model.data_fetch import fetch_stock_data  # Modular import

def show_dashboard(data):
    st.title("Grok Stocks Dashboard")
    st.write("Stock Data:", data)  # Expand to charts later