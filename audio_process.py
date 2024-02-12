import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set

def process_audio(audio_file):
    # Audiodatei laden
    y, _ = librosa.load(audio_file, sr=set.SAMPLE_RATE)  # Setzen der Samplingrate auf den festen Wert

    # Fourier-Transformation durchführen
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Use maximum filter to highlight peaks in the spectrogram
    max_filtered = maximum_filter(D, size=(set.PEAK_BOX_SIZE, set.PEAK_BOX_SIZE), mode='constant', cval=-np.inf)

    # Get indices of peaks
    peaks_indices = np.argwhere((D == max_filtered) & (D > set.MIN_DB_FILTER))

    # Zeit-Frequenz-Darstellung erstellen
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Plot the original spectrogram
    img_original = librosa.display.specshow(D, sr=set.SAMPLE_RATE, x_axis='time', y_axis='log', ax=ax[0])
    ax[0].set_title('Original Spectrogram')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Frequency')
    plt.colorbar(img_original, format='%+2.0f dB')

    # Downsampling the peaks_indices array to reduce the number of points
    

    # Constellation map with downsampled points
    ax[1].scatter(peaks_indices[:, 1], peaks_indices[:, 0], c='r', marker='o', s=5)
    ax[1].set_title('Constellation Map (Downsampled)')
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('Frequency')

    return fig, peaks_indices

def create_hashes(peaks_indices, time_resolution, frequency_resolution, delay):
    hashes = []
    for i, anchor_point in enumerate(peaks_indices):
        for j, target_point in enumerate(peaks_indices[i + 1:], start=i+1):
            # Prüfen, ob der Ziel-Punkt innerhalb der Zeit- und Frequenzauflösung um den Ankerpunkt liegt
            if (target_point[0] - anchor_point[0]) >= delay and abs(target_point[0] - anchor_point[0] - delay) <= time_resolution and abs(target_point[1] - anchor_point[1]) <= frequency_resolution:

                # Hash-Tupel erstellen: (freq_A, freq_B, zeit_delta)
                hash_tuple = (anchor_point[1], target_point[1], target_point[0] - anchor_point[0])
                # Das Hash-Tupel der Liste der Hashes hinzufügen
                hashes.append(hash_tuple)
    return hashes
