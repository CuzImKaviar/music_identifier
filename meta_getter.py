from serializer import Serializable
import requests
from urllib.parse import quote_plus
from ytmusicapi import YTMusic
# from song import Song


class Song_Metadata():
    ytmusic = YTMusic()
    
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.album = "dummy"
        self.date = "dummy"
        self.duration = "dummy"
        self.cover = "dummy"

    @classmethod
    def get_metadata(cls, title : str, artist : str):
        '''
        Findes a Song
        '''

        query = f"{title} {artist}" if artist else title

        results = cls.ytmusic.search(
            query,
            filter="songs",
            scope=None,
            limit=20
        )

        song = next((r for r in results if title.lower() in r['title'].lower()), None)
        album = cls.ytmusic.get_album(song['album']['id'])
        songinfo = cls.ytmusic.get_song(song['videoId'])['videoDetails']

        return {
            'album': song['album']['name'],
            'album_id': song['album']['id'],
            'song_id': song['videoId'],
            'duration': song['duration'],
            'year': album['year'],
            'viewCount' : songinfo['viewCount'],
            'cover': songinfo['thumbnail']['thumbnails'][-1]['url']
            }

    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    
if __name__ == "__main__":
    
    title = "Ghost Division"
    artist = "Sabaton"

    result = Song_Metadata.get_metadata(title, artist)
    for x in result:
        print (x,':',result[x])

    pass