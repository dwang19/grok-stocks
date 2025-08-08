import streamlit as st  # For writing to GUI if needed

from model.data_fetch import fetch_stock_data  # Import from Model (add if missing)
from view.dashboard import show_dashboard     # Import from View (add if missing)

def run_app(api_key):
    ticker = "AAPL"  # Example; later add user input
    data = fetch_stock_data(ticker, api_key)  # Calls Model
    show_dashboard(data)  # Calls View
    st.write("Controller running successfully!")  # Test message