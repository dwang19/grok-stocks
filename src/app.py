import streamlit as st  # For the GUI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controller.main_controller import run_app

# Call the controller's function
run_app("LDiiM49r7iMvISQyQ7NlY03Glm7K6v_i")  # Replace with your Polygon.io key