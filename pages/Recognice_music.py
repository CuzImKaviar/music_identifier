import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set
from audio_process import fingerprint_file
from audio_process import fingerprint_audio
from audio_process import plot_all
from audio_recorder_streamlit import audio_recorder
from song import Song



# -------------- SETTINGS --------------
page_title = "Recognice"
page_icon = ":musical_note:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"



st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)
    

option = st.radio(
    'Wählen Sie eine Option:',
    ('Upload file for music recognition', 'Microphone-based music recognition'))

if option == 'Upload file for music recognition':

    with st.form("mic-based", clear_on_submit=True):
        audio = st.file_uploader("Upload an audio clip", type=["mp3", "wav"])
        submitted = st.form_submit_button("Song erkennen")

    if audio and submitted:
        hashes = fingerprint_file(audio)
        #fig = plot_all(audio, hashes)
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

elif option == 'Microphone-based music recognition':

    with st.form("mic-based", clear_on_submit=True):
        audio_bytes = audio_recorder(energy_threshold=(-1.0, 1.0), pause_threshold=5.0, sample_rate=41_000)
        if audio_bytes:    
            audio = st.audio(audio_bytes, format="audio/wav")
        submitted = st.form_submit_button("Song erkennen")
    if submitted:
        
        hashes = fingerprint_audio(audio_bytes)
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
