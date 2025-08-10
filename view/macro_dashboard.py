import streamlit as st
from .widgets.treasury_yield_widget import treasury_yield_widget  # Import from subfolder

def show_macro_dashboard():
    st.title("Macro Dashboard")
    st.write("Overview of market environment for position trades.")
    treasury_yield_widget('LDiiM49r7iMvISQyQ7NlY03Glm7K6v_i')  # Call the widget with your API key