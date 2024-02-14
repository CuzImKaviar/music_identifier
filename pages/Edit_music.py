import streamlit as st
#from songs import Song
import sqlite3


# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

con = sqlite3.connect('database.db')
cursor = con.cursor()
cursor.execute("SELECT name FROM songs")
all_song_names = cursor.fetchall()
print(all_song_names)

    

with st.form("delete_form", clear_on_submit=True):
    song_to_delete_title = st.selectbox('Song auswählen',options = all_song_names, key="title")

    submitted = st.form_submit_button("Titel löschen")
    if submitted:
        print("Song to delete: ", song_to_delete_title)
        #cursor.execute("SELECT artist FROM songs WHERE name=?", (song_to_delete_title,))
        #song_to_delete_artist = cursor.fetchall()
        
        #song_to_delete_title_artist = song_to_delete_title + "_" + song_to_delete_artist[0]
        cursor.execute("DELETE FROM songs WHERE name=?", (song_to_delete_title))
        
        #cursor.execute("DROP TABLE {}".format(song_to_delete_title_artist))
        con.commit()
        con.close()
