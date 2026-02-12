import streamlit as st
import subprocess
import time
import requests

st.set_page_config(layout="wide")

# Run Flask app
if "server_started" not in st.session_state:

    subprocess.Popen(["python", "flask/app.py"])

    st.session_state.server_started = True

    # wait for flask to start
    for _ in range(10):
        try:
            requests.get("http://127.0.0.1:5000")
            break
        except:
            time.sleep(1)

# Embed Flask site
st.components.v1.iframe(
    "http://127.0.0.1:5000",
    height=900,
    scrolling=True
)
