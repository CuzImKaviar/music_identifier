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
import requests
from urllib.parse import quote_plus

def search_youtube_video(song_name, artist_name):
    query = f"{song_name} {artist_name} official music video"
    url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
    response = requests.get(url)
    if response.status_code == 200:
        video_id = None
        start_index = response.text.find('{"videoRenderer":{"videoId":"')
        if start_index != -1:
            end_index = response.text.find('"', start_index + 30)
            video_id = response.text[start_index + 29:end_index]
        if video_id:
            return f"https://www.youtube.com/watch?v={video_id}"
    return None


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
    fig, indices, times = process_audio(audio)
    hashmap = create_hashes_v1(indices, times)
    st.pyplot(fig)
    detected_song = Song.identify(hashmap)
    st.write(detected_song)

    song_name = detected_song.title
    artist_name = detected_song.artist
    video_link = search_youtube_video(song_name, artist_name)
    if video_link:
        st.write("YouTube Video Link:", video_link)
    else:
        st.write("Kein passendes Video gefunden.")
       

