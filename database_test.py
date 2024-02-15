import sqlite3

name_of_Song = "song1"
name_of_Artist = "artist1"

audio = name_of_Song + "_" + name_of_Artist

con = sqlite3.connect('database.db')

cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS {} ('anchor point' INTEGER, 'target point' INTEGER, 'delta time' INTEGER, time INTEGER)".format(audio))

con.commit()

con.close()

'''
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
