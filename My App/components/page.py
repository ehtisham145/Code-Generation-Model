import streamlit as st

def show_page():
    # --- Page Configuration ---
    st.set_page_config(
        page_title="Ehtisham Code Generator",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    st.title("💻 Ehtisham Code Generator")
    st.markdown("<p style='font-size:20px;'>Describe what you want to build, and I'll generate the code for you!</p>", unsafe_allow_html=True)
    # --- Custom CSS Styling ---
    st.markdown("""
    <style>
        /* Main app background */
        .main {
            background-color: #0e1117;
            color: #fafafa;
        }

        /* Title Styling */
        .title {
            text-align: center;
            color: #4CAF50;
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #b0b0b0;
            margin-bottom: 40px;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #1a1d23;
        }

        /* Buttons */
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 0.6em 1.2em;
            border-radius: 8px;
            font-weight: 600;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background-color: #3e8e41;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: gray;
            font-size: 14px;
            margin-top: 50px;
        }
    </style>
    """, unsafe_allow_html=True)
