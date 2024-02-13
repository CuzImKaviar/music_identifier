import os
from tinydb import TinyDB, Query
from database_start import DatabaseConnector
from serializer_data import Serializable

class Song(Serializable):

    def get_db_connector(self):
        return DatabaseConnector().get_songs_table()
    
    @classmethod
    def get_all_names(cls):
        return [song['title'] for song in Song.get_db_connector(Song)]

    @classmethod
    def get_all_ids(cls):
        return [song['id'] for song in Song.get_db_connector(Song)]

    def __init__(self, title, hashes) -> None:

        super().__init__(title)
        
        self.title = title
        self.hashes = hashes
 

    @classmethod
    def load_data_by_id(cls, id):
        query = Query()
        result = cls.get_db_connector(cls).search(query.id == id)
        if result:
            data = result[0]
            return cls(data['title'], data['hashes'])
        else:
            return None
    
    @classmethod
    def load_data_by_title(cls, title):
        query = Query()
        result = cls.get_db_connector(cls).search(query.title == title)
        if result:
            data = result[0]
            return cls(data['title'], data['hashes'])
        else:
            return None
        

    def __str__(self):
        return f'Song: {self.title} ({self.hashes})'

    def __repr__(self):
        return self.__str__()

###########################################################################################
if __name__ == "__main__":
    # Create a device
    print(User.get_all_names())
    print(User.get_all_ids())
    user1 = User("one@mci.edu", "User One", "Innsbruck", "Student")
    user2 = User("two@mci.edu", "User Two", "Imst", "Student") 
    user3 = User("three@mci.edu", "User Three", "Landeck", "Student") 
    user1.store()
    user2.store()
    user3.store()
    user1.delete()
    user4 = User("four@mci.edu", "User Four", "Landeck", "Professor") 
    user4.store()

    print(User.get_all_names())
    print(User.get_all_ids())

    loaded_user = User.load_data_by_id('four@mci.edu')
    if loaded_user:
        print(f"Loaded: {loaded_user}")
    else:
        print("User not found.")