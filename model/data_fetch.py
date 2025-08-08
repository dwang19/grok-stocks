import requests  # For API calls (install if needed: pip install requests)

def fetch_stock_data(ticker, api_key):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2024-01-01/2024-08-08?apiKey={api_key}"
    response = requests.get(url)
    return response.json()  # Returns data like EPS or prices