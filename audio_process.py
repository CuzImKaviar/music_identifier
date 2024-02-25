import matplotlib.pyplot as plt
import uuid
import numpy as np
import librosa
from scipy.ndimage import maximum_filter
import settings


def file_to_spectrogram(filename):
    """Calculates the spectrogram of a file."""
    audio, _ = librosa.load(filename, sr=settings.SAMPLE_RATE, mono=True)
    n_fft = int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE)
    return librosa.stft(audio, n_fft=n_fft)


def find_peaks(spectogram):
    """Finds peaks in a spectrogram."""
    data_max = maximum_filter(np.abs(spectogram), size=settings.PEAK_BOX_SIZE, mode='constant', cval=0.0)
    peak_goodmask = (np.abs(spectogram) == data_max)
    y_peaks, x_peaks = peak_goodmask.nonzero()
    peak_values = np.abs(spectogram)[y_peaks, x_peaks]
    i = peak_values.argsort()[::-1]
    j = [(y_peaks[idx], x_peaks[idx]) for idx in i]
    total = np.abs(spectogram).shape[0] * np.abs(spectogram).shape[1]
    peak_target = int((total / (settings.PEAK_BOX_SIZE**2)) * settings.POINT_EFFICIENCY)
    return j[:peak_target]


def idxs_to_tf_pairs(idxs, t, f):
    """Helper function to convert time/frequency indices into values."""
    return np.array([(f[i[0]], t[i[1]]) for i in idxs])


def hash_point_pair(p1, p2):
    """Helper function to generate a hash from two time/frequency points."""
    return hash((p1[0], p2[0], p2[1]-p2[1]))


def target_zone(anchor, points, width, height, t):
    """Generates a target zone as described in `the Shazam paper
    <https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf>`_.

    Given an anchor point, yields all points within a box that starts `t` seconds after the point,
    and has width `width` and height `height`.

    :param anchor: The anchor point
    :param points: The list of points to search
    :param width: The width of the target zone
    :param height: The height of the target zone
    :param t: How many seconds after the anchor point the target zone should start
    :returns: Yields all points within the target zone.
    """
    x_min = anchor[1] + t
    x_max = x_min + width
    y_min = anchor[0] - (height*0.5)
    y_max = y_min + height
    for point in points:
        if point[0] < y_min or point[0] > y_max:
            continue
        if point[1] < x_min or point[1] > x_max:
            continue
        yield point


def hash_points(points):
    """Generates all hashes for a list of peaks.

    Iterates through the peaks, generating a hash for each peak within that peak's target zone.

    :param points: The list of peaks.
    :param filename: The filename of the song, used for generating song_id.
    :returns: A list of tuples of the form (hash, time offset, song_id).
    """
    hashes = []
    for anchor in points:
        for target in target_zone(
            anchor, points, settings.TARGET_T, settings.TARGET_F, settings.TARGET_START
        ):
            hashes.append((
                # hash
                hash_point_pair(anchor, target),
                # time offset
                anchor[1],
            ))
    return hashes


def fingerprint_file(filename):
    """Generate hashes for a file.

    Given a file, runs it through the fingerprint process to produce a list of hashes from it.

    :param filename: The path to the file.
    :returns: Hash points.
    """
    spectogram = file_to_spectrogram(filename)
    t = librosa.frames_to_time(np.arange(spectogram.shape[1]))
    f = librosa.fft_frequencies(sr=settings.SAMPLE_RATE, n_fft=int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE))
    peaks = find_peaks(spectogram)
    peaks = idxs_to_tf_pairs(peaks, t, f)
    return hash_points(peaks)


def fingerprint_audio(frames):
    """Generate hashes for a series of audio frames.

    Used when recording audio.

    :param frames: A mono audio stream. Data type is any that ``scipy.signal.spectrogram`` accepts.
    :returns: The output of :func:`hash_points`.
    """
    n_fft = int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE)
    spectogram = librosa.stft(frames, n_fft=n_fft)
    t = librosa.frames_to_time(np.arange(spectogram.shape[1]))
    f = librosa.fft_frequencies(sr=settings.SAMPLE_RATE, n_fft=int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE))
    peaks = find_peaks(spectogram)
    peaks = idxs_to_tf_pairs(peaks, t, f)
    return hash_points(peaks, "recorded")

def plot_all(filename, hashes):
    """Plot a spectrogram, a maximum filtered spectrogram and a constellation map."""
    # Calculate the spectrogram of the file
    spectrogram = file_to_spectrogram(filename)

    # Find peaks in the spectrogram
    peaks = find_peaks(spectrogram)

    # Maximum filtered spectrogram
    data_max = maximum_filter(np.abs(spectrogram), size=settings.PEAK_BOX_SIZE, mode='constant', cval=0.0)

    fig, ax = plt.subplots(3, 1, figsize=(10, 12))

    # Plot the original spectrogram
    img_original = librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), sr=settings.SAMPLE_RATE, x_axis='time', y_axis='log', ax=ax[0])
    ax[0].set_title('Original Spectrogram')
    ax[0].set_xlabel('Time (falsch aber ich bekommes es nicht gefixed)')
    ax[0].set_ylabel('Frequency')
    fig.colorbar(img_original, ax=ax[0], format='%+2.0f dB')

    # Plot the filtered spectrogram to highlight peaks
    img_filtered = librosa.display.specshow(librosa.amplitude_to_db(data_max, ref=np.max), sr=settings.SAMPLE_RATE, x_axis='time', y_axis='log', ax=ax[1])
    ax[1].set_title('Filtered Spectrogram (Peaks Highlighted)')
    ax[1].set_xlabel('Time (falsch aber ich bekommes es nicht gefixed)')
    ax[1].set_ylabel('Frequency')
    fig.colorbar(img_filtered, ax=ax[1], format='%+2.0f dB')

    # Constellation map with downsampled points
    # Convert hashes to points
    points = [(hash[1], hash[0]) for hash in hashes]
    ax[2].scatter(*zip(*points))
    ax[2].set_title('Constellation Map (Downsampled)')
    ax[2].set_xlabel('Time (die stimmt)')
    ax[2].set_ylabel('Frequency')

    plt.tight_layout()
    return fig