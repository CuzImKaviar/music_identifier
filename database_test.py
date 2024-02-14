import sqlite3

name_of_Song = "song1"
name_of_Artist = "artist1"

audio = name_of_Song + "_" + name_of_Artist

con = sqlite3.connect('database.db')

cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS {} ('anchor point' INTEGER, 'target point' INTEGER, 'delta time' INTEGER, time INTEGER)".format(audio))

con.commit()

con.close()
