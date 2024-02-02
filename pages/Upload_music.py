import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# -------------- SETTINGS --------------
page_title = "Upload music"
page_icon = ":microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"




st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)




# Datei hochladen
audio = st.file_uploader("Upload an audio file", type=["mp3"])

if audio:
    # Audiodatei laden
    y, sr = librosa.load(audio, sr=None)

    # Fourier-Transformation durchführen
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Zeit-Frequenz-Darstellung erstellen
    fig, ax = plt.subplots(figsize=(10, 4))
    img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax)
    plt.colorbar(img, format='%+2.0f dB')  # Hier wird img als mappable übergeben
    plt.title('Spectrogram')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    st.pyplot(fig)

    