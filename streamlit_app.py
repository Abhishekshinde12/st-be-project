import streamlit as st

# Set page config to wide mode and fullscreen
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Read your HTML, CSS, and JS files
with open("index.html", "r") as html_file:
    html_content = html_file.read()

with open("style.css", "r") as css_file:
    css_content = css_file.read()

with open("script.js", "r") as js_file:
    js_content = js_file.read()

# Inject custom CSS to make the iframe take full width and height
custom_css = """
<style>
    .stApp {
        margin: 0;
        padding: 0;
    }
    iframe {
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        border: none;
    }
</style>
"""

# Combine everything together
full_content = f"{custom_css}<style>{css_content}</style>{html_content}<script>{js_content}</script>"

# Display the HTML content with Streamlit
st.components.v1.html(full_content, height=1000, scrolling=True)

# Hide Streamlit elements
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
