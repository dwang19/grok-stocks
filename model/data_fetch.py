import requests
from datetime import datetime, timedelta
import pandas as pd  # For organizing data into a table for charting

def fetch_treasury_yields(api_key, days_back=60):  # Extended to 60 for more data
    yields = []  # List to store date and yield data
    end_date = datetime.now().date()  # Today's date
    start_date = end_date - timedelta(days=days_back)  # 60 days ago
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
        url = f"https://api.polygon.io/fed/v1/treasury-yields?date={date_str}&apiKey={api_key}"
        response = requests.get(url)
        print(f"Debug: Date {date_str} - Status: {response.status_code} - Response: {response.text}")  # Temporary debug print
        if response.status_code == 200:  # Successful call
            data = response.json()
            if "results" in data and data["results"]:  # Check for results array and if not empty
                result = data["results"][0]  # First (and usually only) item
                if "yield_10_year" in result:  # The correct key for 10-year yield
                    yields.append({"date": date_str, "yield": result["yield_10_year"]})
        current_date += timedelta(days=1)  # Move to next day
    return pd.DataFrame(yields)  # Convert to a DataFrame (table) for easy charting

# Temporary test (remove after)
if __name__ == "__main__":
    api_key = 'LDiiM49r7iMvISQyQ7NlY03Glm7K6v_i'
    data = fetch_treasury_yields(api_key)
    print(data)