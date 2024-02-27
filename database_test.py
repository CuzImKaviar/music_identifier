import sqlite3

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import settings as set
from audio_process import fingerprint_file
from audio_process import plot_all, plot_waveform, plot_constellation_map, plot_filtered_spectrogram, plot_spectrogram
from song import Song


song_snipped = "C:\\Users\\sebba\\Desktop\\Musik_for_testing\\3_Running_Up_That_Hill_instrumental.wav"
hashes = fingerprint_file(song_snipped)
#print(hashes)
#song = Song("Running up that Hill", "GZUZ", hashes)
#song.delete()
#song.save()
song = Song.identify(hashes)
print(song)

#fig_waveform, fig_spectrogram, fig_filtered_spectrogram, fig_constellation_map = plot_all(song_snipped, hashes)
#fig_waveform.show()
#fig_spectrogram.show()
#fig_filtered_spectrogram.show()
#fig_constellation_map.show()

#fig = plot_waveform(song_snipped)

#fig = plot_spectrogram(song_snipped)

#fig = plot_filtered_spectrogram(song_snipped)

#fig = plot_constellation_map(song_snipped)
#fig.show()

'''
audio = "C:\\Users\\sebba\\Downloads\\audio.mp3"
song_name = "song1"
song_artist = "artist1"

fig, indices, times = process_audio(audio)
hashmap = create_hashes_v1(indices, times)

song = Song(song_name, song_artist, hashmap)
song.save()


name_of_Song = "song1"
name_of_Artist = "artist1"

audio = name_of_Song + "_" + name_of_Artist

con = sqlite3.connect('database.db')

cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS {} ('anchor point' INTEGER, 'target point' INTEGER, 'delta time' INTEGER, time INTEGER)".format(audio))

con.commit()

con.close()


def initialize_database():
    # Connect to the database
    con = sqlite3.connect('database.db')

    # Create a cursor
    cursor = con.cursor()

    # Create a table
    cursor.execute("""CREATE TABLE IF NOT EXISTS songs(
    name text,
    artist text
    )""")


    # Commit the databse
    con.commit()

    # Close the connection
    con.close()

if __name__ == "__main__":
    initialize_database()
'''
