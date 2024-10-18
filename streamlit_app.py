import streamlit as st

# Read your HTML, CSS, and JS files
with open("index.html", "r") as html_file:
    html_content = html_file.read()

with open("style.css", "r") as css_file:
    css_content = f"<style>{css_file.read()}</style>"

with open("script.js", "r") as js_file:
    js_content = f"<script>{js_file.read()}</script>"

# Combine everything together
full_content = css_content + html_content + js_content

# Display the HTML content with Streamlit
# st.components.v1.html(full_content, height=600, scrolling=True)
st.components.v1.html(full_content, height=100%, scrolling=True)
