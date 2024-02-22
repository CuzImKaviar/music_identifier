import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set
from audio_process import process_audio 
from audio_process import create_hashes_v1
from song import Song
import time
import sqlite3


# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

with st.form("entry_form", clear_on_submit=True):
    # Datei hochladen
    song_name = st.text_input("Name des Songs", max_chars=64, placeholder="Name hier einfügen ...", key="Name")
    song_artist = st.text_input("Name des Künstlers", max_chars=64, placeholder="Künstler hier einfügen ...", key="Artist")
    audio = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    submitted = st.form_submit_button("Neuen Song speichern")

if audio and submitted:

    # Startzeitpunkt erfassen
    start_time = time.time()


    fig, indices, times = process_audio(audio)
    hashmap = create_hashes_v1(indices, times) 
    st.pyplot(fig)

    # Endzeitpunkt erfassen
    end_time = time.time()
    # Ausführungszeit berechnen
    execution_time = end_time - start_time
    st.write("Ausführungszeit:", execution_time, "Sekunden")
    print("Ausführungszeit:", execution_time, "Sekunden")


    song = Song(song_name, song_artist, hashmap)
    song.save()
    


