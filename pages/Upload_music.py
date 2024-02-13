import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set
from audio_process import process_audio 
from audio_process import create_hashes
from songs import Song


# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

with st.form("entry_form", clear_on_submit=True):
    # Datei hochladen
    name_of_Song = st.text_input("Name des Songs", max_chars=64, placeholder="Name hier einfügen ...", key="Name")
    audio = st.file_uploader("Upload an audio file", type=["mp3"])
    submitted = st.form_submit_button("Neuen Song speichern")

if audio and submitted:
    fig, indices = process_audio(audio)
    hashmap = create_hashes(indices,set.TARGET_T,set.TARGET_F,set.TARGET_START_DELAY,name_of_Song)
    st.pyplot(fig)
    print(hashmap)#Work in progress
    song = Song(name_of_Song,1)
    song.store()

