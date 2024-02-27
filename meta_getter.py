from serializer import Serializable
import requests
from urllib.parse import quote_plus
from duckduckgo_search import DDGS
from duckduckgo_search import AsyncDDGS


class Song_Metadata():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

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


    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def __repr__(self):
        return self.__str__()
    
if __name__ == "__main__":
    # query = f"Oxygène, Pt. 4 Jean-Michel Jarre official music video"
    # url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
    # response = requests.get(url)
    # if response.status_code == 200:
    #     print(url)

    from duckduckgo_search import DDGS

    with DDGS() as ddgs:
        keywords = 'butterfly'
        ddgs_images_gen = ddgs.images(
            keywords,
            region="wt-wt",
            safesearch="off",
            size=None,
            color="Monochrome",
            type_image=None,
            layout=None,
            license_image=None,
            max_results=100,
        )
        results = [r for r in ddgs_images_gen]

    print(results)
    pass