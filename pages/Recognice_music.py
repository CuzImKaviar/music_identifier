import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set
from audio_process import process_audio 
from song import Song

# -------------- SETTINGS --------------
page_title = "Recognice"
page_icon = ":musical_note:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"




st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


with st.form("Audioausschnitt erkennen", clear_on_submit=True):
    # Datei hochladen
    audio = st.file_uploader("Upload an audio clip", type=["mp3", "wav"])
    submitted = st.form_submit_button("Song erkennen")

if audio and submitted:
    fig, hashmap = process_audio(audio)
    st.pyplot(fig)
    song_snipped = Song(hashmap)
    detected_song = song_snipped.identify_song()
    st.write(detected_song)

