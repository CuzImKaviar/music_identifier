import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set
from audio_process import process_audio 
from audio_process import create_hashes_v1
#from songs import Song

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
    audio = st.file_uploader("Upload an audio file", type=["mp3"])
    submitted = st.form_submit_button("Neuen Song speichern")

if audio and submitted:
    name_artist = song_name + "_" + song_artist
    fig, indices, times = process_audio(audio)
    hashmap = create_hashes_v1(indices, times) 
    st.pyplot(fig)
    #print(hashmap)
    
    converted_hashes = []
    for hash_tuple in hashmap:
        converted_tuple = tuple(int(value) for value in hash_tuple)
        converted_hashes.append(converted_tuple)
    

    con = sqlite3.connect('database.db')

    cursor = con.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS songs(
    name text,
    artist text
    )""")
    cursor.execute("INSERT INTO songs(name, artist) VALUES (?, ?)", (song_name, song_artist))
    
    cursor.execute("CREATE TABLE IF NOT EXISTS {} ('anchor point' INTEGER, 'target_point' INTEGER, 'delta time' INTEGER, time INTEGER)".format(name_artist))
    for hash in converted_hashes:
        cursor.execute("INSERT INTO {} ('anchor point', 'target_point', 'delta time', time) VALUES (?, ?, ?, ?)".format(name_artist), hash)
    con.commit()
    con.close()


