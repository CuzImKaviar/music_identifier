# settings.py

# Abtastfrequenz
SAMPLE_RATE = 44100

# Größe des FFT-Fensters
FFT_WINDOW_SIZE = 0.025  # 25 ms

# Größe des Peak-Box-Filters
PEAK_BOX_SIZE = 5

# Punkt-Effizienz für die Berechnung der Ziel-Peaks
POINT_EFFICIENCY = 0.5

# Zeit für den Beginn der Zielzone
TARGET_START = 1.0

# Breite der Zielzone in Sekunden
TARGET_T = 5.0

# Höhe der Zielzone in Hz
TARGET_F = 5000
