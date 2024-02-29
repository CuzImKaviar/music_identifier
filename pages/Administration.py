import streamlit as st
from song import Song
import pandas as pd

# -------------- SETTINGS --------------
page_title = "Administration"
page_icon = ":gear:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# -------------- SESSION STATES --------------
if "success" not in st.session_state:
    st.session_state["success"] = ""

all_songs = Song.get_all_songs()

# -------------- SORT SONGS BY TITLE --------------
options = [song.split(" by ") for song in all_songs]
options = pd.DataFrame(options, columns=["Title", "Artist"])
options = options.sort_values("Title")  
options = options["Title"] + " by " + options["Artist"]

# -------------- DELETE SONG --------------
with st.form("delete_form", clear_on_submit=True):
    song_to_delete = st.selectbox('Select a song', options=options, key="title")

    submitted = st.form_submit_button("Delete title")
    if submitted:
        try:
            title, artist = song_to_delete.split(" by ")
            song = Song(title, artist, [])
            song.delete()
            st.session_state["success"] = f"{title} by {artist} was successfully deleted!"
            st.rerun()
        except Exception as e:
            st.write(f"Error deleting {song_to_delete}: {e}")

if st.session_state["success"] != "" :        
    st.success(st.session_state["success"])

# -------------- SHOW ALL SONGS --------------
if len(all_songs) != 0:
    song_data = [song.split(" by ") for song in all_songs]
    df = pd.DataFrame(song_data, columns=["Title", "Artist"])
    df = df.sort_values("Title")
    df.index.name = "ID"
    st.dataframe(df, use_container_width=True)
else:
    st.error("No songs available in database!")
