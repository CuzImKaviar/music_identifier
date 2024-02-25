import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set
from audio_process import fingerprint_file
from song import Song



# -------------- SETTINGS --------------
page_title = "Recognice"
page_icon = ":musical_note:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"



st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


with st.form("Audioausschnitt erkennen", clear_on_submit=True):
    audio = st.file_uploader("Upload an audio clip", type=["mp3", "wav"])
    submitted = st.form_submit_button("Song erkennen")

if audio and submitted:

    
    hashes = fingerprint_file(audio)
    #st.pyplot(fig)
    detected_song = Song.identify(hashes)

    if detected_song:
        video_link = detected_song.search_youtube_video()
        if video_link:
            st.video(video_link)
            st.write(detected_song)
            st.write("YouTube Video Link:", video_link)
        else:
            st.write(detected_song)
            st.write("Kein passendes Video gefunden.")
    else:
        st.error("Song konnte nicht erkannt werden.")
       

