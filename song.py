import sqlite3
from database import DatabaseClient
from serializer import Serializable


class Song(Serializable):
    
    def __init__(self, title=None, artist=None, hashmap=None):
        super().__init__()
        self.title = title
        self.artist = artist
        self.hashmap = hashmap if hashmap is not None else []
        self.db = DatabaseClient()
    
    def save(self):
        """
        Save the song to the database.
        """
        print("Song saved: ", self)
        
        self.serialize("songs", ["title", "artist"])
        table_name = f"Hashmap_{self.title}_{self.artist}"
        self.serialize(table_name, ["anchor_point", "target_point", "delta_time", "time"], self.hashmap)
    
        Serializable().close()

    def delete(self):
        """
        Delete the song from the database.
        """
        print("Song deleted: ", self)

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
    
    @classmethod
    def identify(cls, hashmap):
        """
        Identify the song based on its hashmap.
        """
        all_songs = Serializable().deserialize("songs", ["title", "artist"])
        best_match = None
        best_match_count = 0
        
        for song in all_songs:
            table_name = f"Hashmap_{song['title']}_{song['artist']}"
            table_name = table_name.replace(' ', '_')
            
            
            match_count = Serializable().count_matching_hashes(table_name, hashmap)
            if match_count > best_match_count:
                best_match = song
                best_match_count = match_count
        print(song)
        return best_match

    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    


if __name__ == "__main__":
    import sqlite3

    import numpy as np
    import librosa
    import librosa.display
    import matplotlib.pyplot as plt
    from scipy.ndimage import maximum_filter
    import settings as set
    from audio_process import process_audio 
    from audio_process import create_hashes_v1

    song_snipped = "C:\\Users\\sebba\\Downloads\\CantinaBand3.wav"
    fig, indices, times = process_audio(song_snipped)
    hashmap = create_hashes_v1(indices, times)
    
    

    detected_song = Song.identify(hashmap)
    print(detected_song)