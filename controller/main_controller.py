from model.data_fetch import fetch_stock_data
from view.dashboard import show_dashboard

def run_app(api_key):
    ticker = "AAPL"  # Later: Get from user input
    data = fetch_stock_data(ticker, api_key)
    show_dashboard(data)