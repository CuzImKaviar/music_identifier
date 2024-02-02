import streamlit as st

# --- Home Page ---
page_title = "Shazam clone"
page_icon = ":house:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


col1, col2 = st.columns(2)
if col1.button("Upload Music", use_container_width=True):
    st.switch_page("pages/Upload_music.py")   
if col2.button("Recognice Music", use_container_width=True):
    st.switch_page("pages/Recognice_music.py")  