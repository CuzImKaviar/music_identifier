# settings.py

# Abtastfrequenz
SAMPLE_RATE = 44100

#MIN DB FILTER
MIN_DB_FILTER = -45#-50

# Größe des Peak-Box-Filters
PEAK_BOX_SIZE = 30 #30

# Höhe der Zielzone in Hz
TARGET_F = float(4000)  #4000

TARGET_T = float(1.8)  #1.8

TARGET_START_DELAY = float(0.05)

FFT_WINDOW_SIZE = 1024#2048
# How many seconds after an anchor point to start the target zone for pairing.
