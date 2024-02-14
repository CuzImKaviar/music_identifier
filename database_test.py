import sqlite3

con = sqlite3.connect('database.db')

cursor = con.cursor()

song_name = "song1"

cursor.execute("CREATE TABLE IF NOT EXISTS {} (Hash1 INTEGER, Hash2 INTEGER)".format(song_name))

