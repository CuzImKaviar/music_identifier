import sqlite3
from database import DatabaseClient
from serializer import Serializable


class Song(Serializable):
    
    def __init__(self, title, artist, hashes):
        self.title = title
        self.artist = artist
        self.hashes = hashes
    
    def save(self):
        """
        Save the song to the database.
        """
        db = DatabaseClient()
        db.insert(self, "songs", ["title", "artist"])


    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    


if __name__ == "__main__":
    song = Song("song1", "artist1", "hashes1")
    song.serialize(song, "songs", ["title", "artist", "hashes"])
    song.save()
    