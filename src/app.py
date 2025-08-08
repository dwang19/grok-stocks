import streamlit as st  # For the GUI
import sys
import os

# Helper to add the root folder to Python's search path (best practice for modular imports)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controller.main_controller import run_app  # Absolute import (no '..')

# Call the controller's function
run_app("LDiiM49r7iMvISQyQ7NlY03Glm7K6v_i")  # Replace "your_api_key" with your actual Polygon.io key