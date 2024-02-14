import sqlite3

class DatabaseClient:
    """
    Database client connection + Functionen um sachen zu inserten, updaten, deleten
    """
    # Turns the class into a naive singleton
    # --> not thread safe and doesn't handle inheritance particularly well
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.path = sqlite3.connect('database.db')

        return cls.__instance
    
    def get_songs_table(self) -> Table:
        return TinyDB(self.__instance.path, storage=serializer).table('songs')
    
serializer = SerializationMiddleware(JSONStorage)


def initialize_database():
    # Connect to the database
    con = sqlite3.connect('database.db')

    # Create a cursor
    cursor = con.cursor()

    # Create a table
    cursor.execute("""CREATE TABLE IF NOT EXISTS songs(
    name text,
    artist text
    )""")


    # Commit the databse
    con.commit()

    # Close the connection
    con.close()

if __name__ == "__main__":
    initialize_database()
