import streamlit as st
import time
from song import Song
from audio_process import fingerprint_file
from audio_process import create_tempfile
from audio_process import plot_waveform

# -------------- SETTINGS -------------- #
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# -------------- UPLOAD MUSIC -------------- #
with st.form("entry_form", clear_on_submit=True):
    song_name = st.text_input("Name of the song", max_chars=64, placeholder="Insert name here ...", key="Name")
    song_artist = st.text_input("Name of the artist", max_chars=64, placeholder="Insert artist here ...", key="Artist")
    audio = st.file_uploader("Upload an audio file", type=["mp3", "wav"])           
    submitted = st.form_submit_button("Save new song")


# -------------- PROCESS AUDIO -------------- #
if audio and submitted:
    
    # ------------ CONVERT MP3 TO WAV -------------- #
    try:
        if audio.type == "audio/mp3":
            audio = Song.mp3_to_wav(audio)
    except Exception as e:
        st.error(f"Error converting the audio file: {e}")
        print(f"Error converting the audio file: {e}")


    # ------------ START EXECUTION TIME -------------- #
    start_time = time.time()


    # ------------ FINGERPRINT AUDIO -------------- #
    try:
        hashes = fingerprint_file(audio)
    except Exception as e:
        st.error(f"Error creating the fingerprint: {e}")
        print(f"Error creating the fingerprint: {e}")


    # ------------ CALCULATE EXECUTION TIME -------------- #
    try:
        end_time = time.time()
        execution_time = end_time - start_time
        st.write("Execution time to create Fingerprint:", execution_time, "seconds")
        print("Execution time to create Fingerprint:", execution_time, "seconds")
    except Exception as e:
        st.error(f"Error calculating the execution time: {e}")
        print(f"Error calculating the execution time: {e}")


    # ------------ PLOT WAVEFORM -------------- #
    try:
        tempfile = create_tempfile(audio)
        fig = plot_waveform(tempfile)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error plotting the waveform: {e}")
        print(f"Error plotting the waveform: {e}")


    # ------------ SAVE SONG -------------- #
    try:
        song = Song(song_name, song_artist, hashes)
        song.save()
        st.success(f"{song_name} by {song_artist} was successfully saved!")
    except Exception as e:
        st.error(f"Error saving the song: {e}")
        print(f"Error saving the song: {e}")