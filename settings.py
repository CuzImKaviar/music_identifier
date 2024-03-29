""" Settings file for the application """
import warnings

SAMPLE_RATE = 44100
""" File gets resampled to this sample rate """

PEAK_BOX_SIZE = 35
""" Size of the box for the maximum filter """

POINT_EFFICIENCY = 0.8
""" Number of peaks for each file, number between 0 and 1 """

TARGET_START = 0.05 
""" Seconds after anchor point to start target point search """

TARGET_T = 1.8
""" Time resolution for the hash map """

TARGET_F = 4000
""" Frequency resolution for the hash map, number between 0 and 0.5 * SAMPLE_RATE """

FFT_WINDOW_SIZE = 0.2
""" Size of the FFT window in seconds """

MIN_SCORE = 10
""" Minimum score for a match """

def ignore_warnings_pydub():
    """ Ignore warnings from pydub """
    warnings.filterwarnings("ignore", category=RuntimeWarning, module="pydub")
