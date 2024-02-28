from ytmusicapi import YTMusic
# from song import Song

class Song_Metadata():
    ytmusic = YTMusic()
    
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

        data = Song_Metadata.get_metadata(self.title, self.artist)

        self.album = data['album']
        self.album_id = data['album_id']
        self.song_id = data['song_id']
        self.duration = data['duration']
        self.year = data['year']
        self.viewCount = data['viewCount']
        self.cover = data['cover']
    
    def print_infos(self):
        attrs = vars(song)
        print('\n'.join("%s: %s" % item for item in attrs.items()))
        
    @classmethod
    def get_metadata(cls, title : str, artist : str):
        '''
        Findes a song using a unofficial API for YouTube Music and returns relevant meta data for the song

        For more infos about the API see https://ytmusicapi.readthedocs.io/en/stable/index.html 
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

    song = Song_Metadata(title, artist)
    song.print_infos()

    pass