import streamlit as st

st.title("Grok Stocks - Starter App")
st.write("Welcome! This is our modular position trading dashboard.")

# Modular placeholder function (e.g., for future screening module)
def get_sample_data():
    return "Sample data: RSI = 50 (from future Polygon.io fetch)"

st.write(get_sample_data())