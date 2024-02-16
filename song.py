import sqlite3
from database import DatabaseClient
from serializer import Serializable


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

    def delete(self):
        """
        Delete the song from the database.
        """
        self.delete_entry("songs", "title", self.title)
        table_name = f"Hashmap_{self.title}_{self.artist}"
        self.remove_table(table_name)

        Serializable().close()
    
    @classmethod
    def get_all_songs(cls):
        """
        Get all songs from the database.
        """
        songs = Serializable().deserialize("songs", ["title", "artist"])
        formatted_songs = []
        for song in songs:
            formatted_song = f"{song['title']} by {song['artist']}"
            formatted_songs.append(formatted_song)
        return formatted_songs
    
    def identify_song(self):
        """
        Identify the song based on its hashmap.
        """
        all_songs = self.get_all_songs()
        best_match = None
        best_match_count = 0

        for song in all_songs:
            table_name = f"Hashmap_{song['title']}_{song['artist']}"
            song_hashmap = Serializable().deserialize(table_name, ["anchor_point", "target_point", "delta_time", "time"])
            
            match_count = sum(1 for point in self.hashmap if point in song_hashmap)

            if match_count > best_match_count:
                best_match = song
                best_match_count = match_count

        return best_match


    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    


if __name__ == "__main__":
    hashmap = [(1, 2, 3, 4), (5, 6, 7, 8)]
    song1 = Song("title1", "artist1", hashmap)
    song1.save()

    song1.delete()