import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "model")))

# Importing page functions
from pages._pages import home, about, github, try_it

# Page routing dictionary
routes = {
    "Home": home.main,
    "Try it out": try_it.main,
    "About": about.main,
    "GitHub": github.main,
}

# Streamlit page configuration
st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/PremKumarAddala/brain-tumor-detection",
        "Report a bug": "https://github.com/PremKumarAddala/brain-tumor-detection/issues",
        "About": "Detecting brain tumors using *deep Convolutional Neural Networks*",
    },
    initial_sidebar_state="collapsed",
)

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Hide the sidebar toggle button
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a horizontal navigation bar using buttons
st.markdown(
    """
    <style>
        .nav-container {
            display: flex;
            justify-content: center;
            gap: 2rem;
            background-color: #2c3e50;
            padding: 1rem;
            border-radius: 10px;
        }
        .nav-button {
            background-color: transparent;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            padding: 10px 15px;
            border-radius: 5px;
            transition: 0.3s;
        }
        .nav-button:hover {
            background-color: #1abc9c;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create navigation buttons in columns to stay in the same row
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home"):
        st.session_state.current_page = "Home"
with col2:
    if st.button("Try it out"):
        st.session_state.current_page = "Try it out"
with col3:
    if st.button("About"):
        st.session_state.current_page = "About"
with col4:
    if st.button("GitHub"):
        st.session_state.current_page = "GitHub"

# Render the selected page
routes[st.session_state.current_page]()
