import streamlit as st
from song import Song
import sqlite3

# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# -------------- SESSION STATES --------------
if "success" not in st.session_state:
    st.session_state["success"] = ""


all_songs = Song.get_all_songs()    

with st.form("delete_form", clear_on_submit=True):
    song_to_delete = st.selectbox('Select song', options=all_songs, key="title")

    submitted = st.form_submit_button("Delete title")
    if submitted:
        try:
            title, artist = song_to_delete.split(" by ")
            song = Song(title, artist, [])
            song.delete()
            st.session_state["success"] = f"{title} was successfully deleted!"
            st.rerun()
        except Exception as e:
            st.write(f"Error deleting {song_to_delete}: {e}")

if st.session_state["success"] != "" :        
    st.success(st.session_state["success"])