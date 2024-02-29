import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings
from audio_process import fingerprint_file
from audio_process import plot_all
from song import Song
import time

# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

with st.form("entry_form", clear_on_submit=True):
    # Upload file
    song_name = st.text_input("Name of the song", max_chars=64, placeholder="Insert name here ...", key="Name")
    song_artist = st.text_input("Name of the artist", max_chars=64, placeholder="Insert artist here ...", key="Artist")
    audio = st.file_uploader("Upload an audio file", type=["mp3", "wav"])           

    submitted = st.form_submit_button("Save new song")

if audio and submitted:
    try:
        if audio.type == "audio/mp3":
            audio = Song.mp3_to_wav(audio)
    except Exception as e:
        st.write(f"Error converting the audio file: {e}")
        print(f"Error converting the audio file: {e}")

    # Capture start time
    start_time = time.time()

    try:
        hashes = fingerprint_file(audio)
        #fig = plot_all(audio, hashes)
        #st.pyplot(fig)

        # Capture end time
        end_time = time.time()

        # Calculate execution time
        execution_time = end_time - start_time
        st.write("Execution time:", execution_time, "seconds")
        print("Execution time:", execution_time, "seconds")
    except Exception as e:
        st.write(f"Error creating the fingerprint: {e}")
        print(f"Error creating the fingerprint: {e}")

    song = Song(song_name, song_artist, hashes)
    song.save()