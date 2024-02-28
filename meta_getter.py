from serializer import Serializable
import requests
from urllib.parse import quote_plus
from duckduckgo_search import DDGS
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

        result = next((r for r in results if title.lower() in r['title'].lower()), None)



        return cls.ytmusic.get_album(result['album']['id'])
        # return {
        #     'album': result['album']['name'],
        #     'album_id': result['album']['id'],
        #     'song_id': result['videoId'],
        #     'duration': result['duration']}

    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    
if __name__ == "__main__":
    import json
    
    title = "Victory Over Truth"
    artist = "Fox Stevenson"

    # result = Song_Metadata.get_metadata(title, artist)

    query = f"{title} {artist}" if artist else title

    ytmusic = YTMusic()
    results = ytmusic.search(
        query,
        filter="songs",
        scope=None,
        limit=20
    )

    result1 = next((r for r in results if title.lower() in r['title'].lower()), None)

    print(result1['album']['id'])
    result = ytmusic.get_album(result1['album']['id'])
    # for result in results:
    #     print('\n')
    for x in result:
        print (x,':',result[x])

    # print(json.dumps(result, indent=4))

    pass