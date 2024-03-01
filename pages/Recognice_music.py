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
from meta_getter import Metadata


# -------------- DISPLAY META DATA -------------- #
def detecte_Song(audio : bytes) -> None:

    hashes = fingerprint_file(audio)
    detected_song = Song.identify(hashes)

    if detected_song:
        song = Metadata(detected_song.title, detected_song.artist)

        col1, col2 = st.columns([0.45, 0.55], gap="medium")

        with col1:
            st.image(song.cover, f"{song.title} Album Cover")

        with col2:
            info_yt_sptfy = ["Song Infos", "YouTube Music", "Spotify"]
            tab1, tab2, tab3 = st.tabs(info_yt_sptfy)

            with tab1:
                st.write(f"**Title:**      {song.title}")
                st.write(f"**Artist:**     {song.artist}")
                st.write(f"**Album:**      {song.album}")
                st.write(f"**Year:**       {song.year}")
                st.write(f"**Duration:**   {song.duration}")
                st.write(f"**View Count:** {song.viewCount}")

            with tab2:
                st.header(info_yt_sptfy[1])

                
                st.link_button(f"Play song on YouTube Music", song.song_url_YTM, use_container_width=True)

                if song.album_url_YTM:
                    st.link_button(f"Show album on YouTube Music", song.album_url_YTM, use_container_width=True)
                else:
                    st.error("Unable to finde album on YouTube Music with DuckDuckGo!")

            with tab3:
                st.header(info_yt_sptfy[2])

                if song.song_url_sptfy:
                    st.link_button(f"Play song on Spotify", song.song_url_sptfy, use_container_width=True)
                else:
                    st.error("Unable to finde song on Spotify with DuckDuckGo!")

                if song.album_url_sptfy:
                    st.link_button(f"Show album on Spotify", song.album_url_sptfy, use_container_width=True)
                else:
                    st.error("Unable to finde album on Spotify with DuckDuckGo!")
    else:
        st.error("Song konnte nicht erkannt werden.")


# -------------- SETTINGS -------------- #
page_title = "Recognice"
page_icon = ":musical_note:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

# -------------- PAGE -------------- #
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

option = st.radio(
    'Choose an option:',
    ('Upload file for music recognition', 'Microphone-based music recognition'))


# -------------- FILE UPLOAD -------------- #
if option == 'Upload file for music recognition':

    # ------------ FILE UPLOARD FORM -------------- #
    with st.form("file-based", clear_on_submit=True):
        audio = st.file_uploader("Upload an audio clip", type=["mp3", "wav"])
        submitted = st.form_submit_button("Recognize song")

    if submitted:
        detecte_Song(audio) if audio else st.error("No File selected!")


# -------------- MIC INUT -------------- #
elif option == 'Microphone-based music recognition':

    # ------------ MIC INUT -------------- #
    with st.container(border=True):
        audio_bytes = audio_recorder(energy_threshold=(-1.0, 1.0), pause_threshold=6.0, sample_rate=41_000)

        with st.form("mic-based", clear_on_submit=False, border=False):
            if audio_bytes:
                audio = st.audio(audio_bytes, format="audio/wav")
            submitted = st.form_submit_button("Song erkennen")
    
    if submitted:
        detecte_Song(audio_bytes) if audio_bytes else st.error("No Sound Recorded!")
