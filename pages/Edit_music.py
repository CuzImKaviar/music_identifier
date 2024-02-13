import streamlit as st
from songs import Song


# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


Songs_in_databank = Song.get_all_names()

with st.form("delete_form", clear_on_submit=True):
    song_to_deleate_title = st.selectbox('Song auswählen',options = Songs_in_databank, key="user")

    submitted = st.form_submit_button("Titel löschen")
    if submitted:
        song_to_deleate = Song.load_data_by_title(song_to_deleate_title)
        song_to_deleate.delete()