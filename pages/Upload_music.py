import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"




st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)




audio = st.file_uploader("Upload an audio file", type=["mp3"])

