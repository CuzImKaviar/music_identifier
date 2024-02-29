import sqlite3
from database import DatabaseClient
from serializer import Serializable
import requests
import numpy as np
from urllib.parse import quote_plus
from collections import defaultdict
from pydub import AudioSegment
from io import BytesIO
from settings import MIN_SCORE

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
        self.serialize(table_name, ["HASH INTEGER", "Time_Delta REAL"], self.hashmap)
    
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
    
    def search_youtube_video(self):
        query = f"{self.title} {self.artist} official music video"
        url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
        response = requests.get(url)
        if response.status_code == 200:
            video_id = None
            start_index = response.text.find('{"videoRenderer":{"videoId":"')
            if start_index != -1:
                end_index = response.text.find('"', start_index + 30)
                video_id = response.text[start_index + 29:end_index]
            if video_id:
                return f"https://www.youtube.com/watch?v={video_id}"
        return None

    @classmethod
    def mp3_to_wav(cls, audio):
        mp3_bytes = audio.getvalue()
        audio = AudioSegment.from_mp3(BytesIO(mp3_bytes))
        wav_bytes = audio.export(format="wav").read()
        audio_wav = BytesIO(wav_bytes)
        return audio_wav


    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    
############################################################################################################
    @staticmethod
    def score_match(offset_dict):
    
        # Use bins spaced 0.5 seconds apart
        binwidth = 0.5
        offsets = list(offset_dict.values())[0]

        print(F"Offsets: {offset_dict}")

        tks = list(map(lambda x: x[0] - x[1], offsets))
        if len(tks) == 0:
            return 0
        print(F"tks: {tks}")

        hist, _ = np.histogram(tks,
                            bins=np.arange(int(min(tks)),
                                            int(max(tks)) + binwidth + 1,
                                            binwidth))
        print (F"max_hist = {np.max(hist) if len(hist) > 0 else print("0")}")

        return np.max(hist) if len(hist) > 0 and np.max(hist) > MIN_SCORE else 0

    @classmethod
    def best_match(cls, matches):
        matched_song = None
        best_score = 0
        for song_id, offsets in matches.items():
            print(F"Song ID: {song_id}")
            print(F"Offset_dict: {offsets}")
            if not offsets:
                continue
            score = cls.score_match(offsets)
            if score > best_score:
                best_score = score
                matched_song = song_id
        return matched_song


    @classmethod
    def get_matches(cls, table_name, hashes):
        h_dict = {}
        for h, t in hashes:
            h_dict[h] = t
        in_values = f"({','.join([str(h[0]) for h in hashes])})"
        query = f"SELECT HASH, Time_Delta FROM {table_name} WHERE HASH IN {in_values}"
        
        try:
            results = Serializable().execute_query(query)
        except Exception as e:
            print(f"Error fetching results: {e}")

        print(F"Results {table_name}: {len(results)}")
        
        result_dict = defaultdict(list)
        
        for r in results:
            result_dict[table_name].append((r[1], h_dict[r[0]]))
        print(F"Result dict {result_dict}")
        return result_dict
    

    @classmethod
    def identify(cls, hashmap):
        all_songs = Serializable().deserialize("songs", ["title", "artist"])
        matches = {}
        
        for song in all_songs:
            table_name = f"Hashmap_{song['title']}_{song['artist']}"
            table_name = table_name.replace(' ', '_').replace('(', '_').replace(')', '_')
            
            # Get the matching hashes and their time deltas
            matching_hashes = cls.get_matches(table_name, hashmap)
            matches[song['title'], song['artist']] = matching_hashes
            

        best_match = cls.best_match(matches)
        title, artist = best_match
        best_match_song = Song(title, artist)
        print(F"Best match: {best_match_song}, with {len(matches[best_match])} matching hashes.")
        return best_match_song

############################################################################################################

if __name__ == "__main__":
    from audio_process import fingerprint_file
    from serializer import Serializable
    
    audio = "C:\\Users\\sebba\\Desktop\\Musik_for_testing\\3_Welcome_to_The_Internet.wav"
    
    hashes = fingerprint_file(audio)
    #song = Song("6020", "Phlying")
    #song.delete()
    #matches = Song.get_matches("Hashmap_Welcome_To_The_Internet_Bo_Burnham", hashes)
    #best_match = Song.best_match(matches)
    detected_song = Song.identify(hashes)