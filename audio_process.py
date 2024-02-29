import matplotlib.pyplot as plt
import numpy as np
import librosa
from scipy.ndimage import maximum_filter
from scipy.signal import spectrogram
import settings
import tempfile


def file_to_spectrogram(filename):
    """Calculates the spectrogram of a file."""
    audio, _ = librosa.load(filename, sr=settings.SAMPLE_RATE, mono=True)
    nperseg = int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE)
    hop_length = nperseg // 4
    return spectrogram(audio, settings.SAMPLE_RATE, nperseg=nperseg, noverlap=hop_length)


def find_peaks(Sxx):
    """Finds peaks in a spectrogram."""
    data_max = maximum_filter(Sxx, size=settings.PEAK_BOX_SIZE, mode='constant', cval=0.0)
    peak_goodmask = (Sxx == data_max)
    y_peaks, x_peaks = peak_goodmask.nonzero()
    peak_values = Sxx[y_peaks, x_peaks]
    i = peak_values.argsort()[::-1]
    j = [(y_peaks[idx], x_peaks[idx]) for idx in i]
    total = Sxx.shape[0] * Sxx.shape[1]
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
    f, t, Sxx = file_to_spectrogram(filename)
    peaks = find_peaks(Sxx)
    peaks = idxs_to_tf_pairs(peaks, t, f)
    return hash_points(peaks)


def convert_bytes_to_wav(audio_bytes):
    """Converts audio bytes to a temporary wav file. 
    :param audio_bytes: The audio bytes.
    :returns: The path to the temporary wav file.
    """
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

    # Open the temporary file as a wav file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
    # Schreibe den Inhalt in das temporäre Dateiobjekt
        temp_file.write(audio_bytes)
    # Return the path to the temporary wav file
    return temp_file.name


def fingerprint_audio(audio_bytes):
    """Generate hashes for audio bytes."""
    # convert audio bytes to temporary wav file
    wav_file = convert_bytes_to_wav(audio_bytes)

    # create hash points
    return fingerprint_file(wav_file)

#----------------- PLOT FUNCTIONS -----------------#
# create a temporary file used for plotting audio from streamlit
def create_tempfile(audio):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        tmpfile.write(audio.getvalue())
        tmpfile_name = tmpfile.name
    return tmpfile_name

def plot_waveform(audio):
    y, sr = librosa.load(audio)
    fig, ax = plt.subplots(figsize=(10, 4))
    t = np.arange(len(y)) / sr
    t_min_sec = ["%02d:%02d" % (m, s) for m, s in zip(t // 60, t % 60)]
    ax.plot(t, y)
    ax.set_xlim(0, len(y) / sr)
    ax.set_title('Original Waveform')
    ax.set_xlabel('Time [min:sec]')
    ax.set_ylabel('Amplitude [dB]')
    if len(y) / sr > 30:
        ax.set_xticks(t[::sr*30])
        ax.set_xticklabels(t_min_sec[::sr*30])
    else:
        ax.set_xticks(t[::sr])
        ax.set_xticklabels(t_min_sec[::sr])
    plt.tight_layout()
    return fig

def plot_spectrogram(filename):
    f, t, Sxx = file_to_spectrogram(filename)
    fig, ax = plt.subplots(figsize=(10, 4))
    hop_length = int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE) // 4
    img = librosa.display.specshow(librosa.amplitude_to_db(np.abs(Sxx), ref=np.max), sr=settings.SAMPLE_RATE, hop_length=hop_length, x_axis='time', y_axis='log', ax=ax)
    ax.set_title('Original Spectrogram')
    ax.set_xlabel('Time [min:sec]')
    ax.set_ylabel('Frequency [Hz]')
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    plt.tight_layout()
    return fig

def plot_filtered_spectrogram(filename):
    f, t, Sxx = file_to_spectrogram(filename)
    peaks = maximum_filter(np.abs(Sxx), size=settings.PEAK_BOX_SIZE, mode='constant', cval=0.0)
    fig, ax = plt.subplots(figsize=(10, 4))
    hop_length = int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE) // 4
    img = librosa.display.specshow(librosa.amplitude_to_db(np.abs(peaks), ref=np.max), sr=settings.SAMPLE_RATE, hop_length=hop_length, x_axis='time', y_axis='log', ax=ax)
    ax.set_title('Filtered Spectrogram (Peaks Highlighted)')
    ax.set_xlabel('Time [min:sec]')
    ax.set_ylabel('Frequency [Hz]')
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    plt.tight_layout()
    return fig

def plot_constellation_map(filename):
    f, t, Sxx = file_to_spectrogram(filename)
    peaks = find_peaks(Sxx)
    anchor_points = set(tuple(x) for x in idxs_to_tf_pairs(peaks, t, f))

    target_points = set()
    for anchor in anchor_points:
        for target in target_zone(
            anchor, anchor_points, settings.TARGET_T, settings.TARGET_F, settings.TARGET_START
        ):
            target_points.add(target)
    
    target_points = target_points - anchor_points

    hop_length = int(settings.SAMPLE_RATE * settings.FFT_WINDOW_SIZE) // 4
    anchor_points = set([(point[1] / hop_length, point[0]) for point in anchor_points])
    target_points = set([(point[1] / hop_length, point[0]) for point in target_points])
    fig, ax = plt.subplots(figsize=(10, 4))

    if target_points:
        ax.scatter(*zip(*anchor_points), s=5, color='blue', label='Anchor Points')
        ax.scatter(*zip(*target_points), s=5, color='red', label='Target Points')
    else:
        ax.scatter(*zip(*anchor_points), s=5, color='blue', label='Anchor Points & Target Points')
    
    ax.set_title('Constellation Map (Downsampled)')
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Frequency [Hz]')
    ax.legend()
    plt.tight_layout()
    return fig

def plot_all(filename):
    fig, axs = plt.subplots(4, 1, figsize=(10, 16))

    fig_waveform = plot_waveform(filename)
    axs[0].imshow(fig_waveform)

    fig_spectrogram = plot_spectrogram(filename)
    axs[1].imshow(fig_spectrogram)

    fig_filtered_spectrogram = plot_filtered_spectrogram(filename)
    axs[2].imshow(fig_filtered_spectrogram)

    fig_constellation_map = plot_constellation_map(filename)
    axs[3].imshow(fig_constellation_map)

    return fig


if __name__ == "__main__":
    audio = "C:\\Users\\sebba\\Desktop\\Musik_for_testing\\Never_Gonna_Give_You_Up.wav"
    fig = plot_waveform(audio)
    plt.show()
    