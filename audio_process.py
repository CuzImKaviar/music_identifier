import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import settings as set

def process_audio(audio_file):
    # Audiodatei laden
    y, sr = librosa.load(audio_file, sr=set.SAMPLE_RATE)  # Setzen der Samplingrate auf den festen Wert

    # Fourier-Transformation durchführen
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=set.FFT_WINDOW_SIZE)), ref=np.max)

    # Anzahl der Frames im Spectrogramm
    num_frames = D.shape[1]

    # Use maximum filter to highlight peaks in the spectrogram
    max_filtered = maximum_filter(D, size=(set.PEAK_BOX_SIZE, set.PEAK_BOX_SIZE+5), mode='constant', cval=-np.inf)

    # Get indices of peaks
    peaks_indices = np.argwhere((D == max_filtered) & (D > set.MIN_DB_FILTER))

    # Berechne die Dauer eines Frames in Sekunden
    frame_duration = librosa.get_duration(y=y, sr=sr) / num_frames

    # Erzeuge eine Liste von Zeitstempeln für jedes Frame
    times = np.arange(0, num_frames) * frame_duration

    # Zeit-Frequenz-Darstellung erstellen
    fig, ax = plt.subplots(3, 1, figsize=(10, 12))

    # Plot the original spectrogram
    img_original = librosa.display.specshow(D, sr=set.SAMPLE_RATE, x_axis='s', y_axis='log', ax=ax[0])
    ax[0].set_title('Original Spectrogram')
    ax[0].set_xlabel('Time (falsch aber ich bekommes es nicht gefixed)')
    ax[0].set_ylabel('Frequency')
    plt.colorbar(img_original, ax=ax[0], format='%+2.0f dB')

    # Plot the filtered spectrogram to highlight peaks
    img_filtered = librosa.display.specshow(max_filtered, sr=set.SAMPLE_RATE, x_axis='s', y_axis='log', ax=ax[1])
    ax[1].set_title('Filtered Spectrogram (Peaks Highlighted)')
    ax[1].set_xlabel('Time (falsch aber ich bekommes es nicht gefixed)')
    ax[1].set_ylabel('Frequency')
    plt.colorbar(img_filtered, ax=ax[1], format='%+2.0f dB')

    # Constellation map with downsampled points
    ax[2].scatter(times[peaks_indices[:, 1]], peaks_indices[:, 0], c='r', marker='o', s=5)
    ax[2].set_title('Constellation Map (Downsampled)')
    ax[2].set_xlabel('Time (die stimmt)')
    ax[2].set_ylabel('Frequency')

    return fig, peaks_indices,times




def create_hashes_v1(peaks_indices, times):
    time_resolution = set.TARGET_T
    frequency_resolution = set.TARGET_F
    delay = set.TARGET_START_DELAY

    hashes = []
    for i, anchor_point in enumerate(peaks_indices):
        anchor_time = times[anchor_point[1]]  # Zeitpunkt des Ankerpunkts
        for j, target_point in enumerate(peaks_indices[i + 1:], start=i+1):
            target_time = times[target_point[1]]  # Zeitpunkt des Zielpeaks
            # Überprüfen, ob der Zeitpunkt des Zielpeaks später als der Zeitpunkt des Ankerpunkts ist
            if target_time > anchor_time:
                # Prüfen, ob der Ziel-Punkt innerhalb der Zeit- und Frequenzauflösung um den Ankerpunkt liegt
                if (target_point[0] - anchor_point[0]) >= delay and abs(target_point[0] - anchor_point[0] - delay) <= time_resolution and abs(target_point[1] - anchor_point[1]) <= frequency_resolution:
                    # Hash-Tupel erstellen: (freq_A, freq_B, zeit_delta, Zeitpunkt von Ankerpunkt)
                    hash_tuple = (int(anchor_point[1]), int(target_point[1]), target_time - anchor_time, anchor_time)
                    # Das Hash-Tupel der Liste der Hashes hinzufügen
                    hashes.append(hash_tuple)
    return hashes
