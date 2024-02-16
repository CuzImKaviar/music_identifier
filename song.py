import sqlite3
from database import DatabaseClient
from serializer import Serializable
from HashTuple import HashTuple


class Song(Serializable):
    
    def __init__(self, title, artist, hashmap):
        super().__init__()
        self.title = title
        self.artist = artist
        self.hashmap = hashmap
        self.db = DatabaseClient()
    
    def save(self):
        """
        Save the song to the database.
        """
        self.serialize("songs", ["title", "artist"])
        table_name = f"Hashmap_{self.title}_{self.artist}"
        self.serialize(table_name, ["anchor_point", "target_point", "delta_time", "time"], self.hashmap)
    
        Serializable().close()


    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    


if __name__ == "__main__":
    hashmap = [(1, 2, 3, 4), (5, 6, 7, 8)]
    song1 = Song("title1", "artist1", hashmap)
    print(song1.__dict__)
    song1.save()