import streamlit as st
import time
from audio_process import fingerprint_file
from audio_process import fingerprint_audio
from audio_recorder_streamlit import audio_recorder
from song import Song
from meta_getter import Metadata


# -------------- DETECT SONG -------------- #
def detect_Song(hashes : list) -> None:
    
    # ------------ IDENTIFY SONG -------------- #
    try:
        detected_song = Song.identify(hashes)
    except Exception as e:
        st.error(f"Error identifying the song: {e}")
        print(f"Error identifying the song: {e}")

    # ------------ CALCULATE EXECUTION TIME -------------- #
    try:
        end_time = time.time()
        execution_time = end_time - start_time
        st.write("Execution time to compared to Database:", execution_time, "seconds")
        print("Execution time to compared to Database:", execution_time, "seconds")
    except Exception as e:
        st.error(f"Error calculating the execution time: {e}")
        print(f"Error calculating the execution time: {e}")

    # ------------ DISPLAY META DATA -------------- #
    if detected_song:
        st.write(f"Song successfully identified as:")
        st.subheader(f"{detected_song.title} by {detected_song.artist}")

        # ------------ SEARCH META DATA -------------- #
        try:
            song = Metadata(detected_song.title, detected_song.artist)
        except Exception as e:
            st.error(f"Error finging the meta data: {e}")
            print(f"Error finging the meta data: {e}")

        # ------------ DISPLAYING META DATA -------------- #
        col1, col2 = st.columns([0.45, 0.55], gap="medium")

        with col1:
            st.image(song.cover, f"{song.title} Album Cover")

        with col2:
            info_yt_sptfy = ("Song Infos", "YouTube Music", "Spotify")
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
                    st.error("Unable to finde URL to album on YouTube Music with DuckDuckGo!")

            with tab3:
                st.header(info_yt_sptfy[2])

                if song.song_url_sptfy:
                    st.link_button(f"Play song on Spotify", song.song_url_sptfy, use_container_width=True)
                else:
                    st.error("Unable to finde URL to song on Spotify with DuckDuckGo!")

                if song.album_url_sptfy:
                    st.link_button(f"Show album on Spotify", song.album_url_sptfy, use_container_width=True)
                else:
                    st.error("Unable to finde URL to album on Spotify with DuckDuckGo!")
    else:
        st.error("No fitting Song found in database.")


# -------------- SETTINGS -------------- #
page_title = "Recognice"
page_icon = ":musical_note:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# -------------- SELECTION -------------- #
options = ('Upload file for music recognition', 'Microphone-based music recognition')
option = st.radio('Choose an option:', options)

# -------------- FILE UPLOAD -------------- #
if option == options[0]:

    # ------------ FILE UPLOARD FORM -------------- #
    with st.form("file-based", clear_on_submit=True):
        audio = st.file_uploader("Upload an audio clip", type=["mp3", "wav"])
        submitted = st.form_submit_button("Recognize song")

    if submitted and audio:

        # ------------ START EXECUTION TIME -------------- #
        start_time = time.time()

        # ------------ FINGERPRINT FILE -------------- #
        try:
            hashes = fingerprint_file(audio)
        except Exception as e:
            st.error(f"Error creating the fingerprint: {e}")
            print(f"Error creating the fingerprint: {e}")

        # -------------- DETECTING SONG -------------- #
        detect_Song(hashes)

    elif submitted and not audio:
        st.error("No File selected!")


# -------------- MIC INUT -------------- #
elif option == options[1]:

    # ------------ MIC INUT -------------- #
    with st.container(border=True):
        audio_bytes = audio_recorder(energy_threshold=(-1.0, 1.0), pause_threshold=6.0, sample_rate=41_000)

        with st.form("mic-based", clear_on_submit=False, border=False):
            if audio_bytes:
                audio = st.audio(audio_bytes, format="audio/wav")
            submitted = st.form_submit_button("Song erkennen")
    
    if submitted and audio_bytes:

        # ------------ START EXECUTION TIME -------------- #
        start_time = time.time()

        # ------------ FINGERPRINT AUDIO -------------- #
        try:
            hashes = fingerprint_audio(audio_bytes)
        except Exception as e:
            st.error(f"Error creating the fingerprint: {e}")
            print(f"Error creating the fingerprint: {e}")

        # -------------- DETECTING SONG -------------- #
        detect_Song(hashes)

    elif submitted and not audio_bytes:
        st.error("No Sound Recorded!")