import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter

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

    # Use maximum filter to highlight peaks in the spectrogram
    max_filtered = maximum_filter(D, size=(3, 3), mode='constant', cval=-np.inf)

    # Get indices of peaks
    peaks_indices = np.argwhere((D == max_filtered) & (D > -80))

    # Zeit-Frequenz-Darstellung erstellen
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Plot the original spectrogram
    img_original = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax[0])
    ax[0].set_title('Original Spectrogram')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Frequency')
    plt.colorbar(img_original, format='%+2.0f dB')

    # Create a constellation map
    ax[1].scatter(peaks_indices[:, 1], peaks_indices[:, 0], c='r', marker='o', s=5)
    ax[1].set_title('Constellation Map')
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('Frequency')

    st.pyplot(fig)
