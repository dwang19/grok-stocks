import streamlit as st
from model.data_fetch import fetch_treasury_yields  # Absolute import from root

def treasury_yield_widget(api_key):
    st.subheader("10-Year Treasury Yield")
    data = fetch_treasury_yields(api_key)
    if not data.empty:
        st.line_chart(data.set_index("date")["yield"])  # Line chart of yields over time
        latest_yield = data.iloc[-1]["yield"]  # Most recent value
        st.metric("Latest Yield", f"{latest_yield:.2f}%")  # Display as a highlighted number
        st.write("Relevance: Rising yields hurt growth stocks (higher discount rates), creating sector swings—monitor for rotations out of tech into value.")
    else:
        st.error("No data fetched—check API key, date range, or Polygon.io status.")