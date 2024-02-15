import sqlite3
import pickle
from serializer import Serializable

class DatabaseClient(Serializable):
    """
    Database client connection + functiions to insert, update, delete and extract data
    """
    # Turns the class into a naive singleton
    # --> not thread safe and doesn't handle inheritance particularly well
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, db_name='database.db'):
        if self._initialized:
            return
        super().__init__(db_name)
        self._initialized = True

    #def insert(self, table_name, columns):
    #    """
    #    Insert data into the database.
    #    """
    #    self.serialize(table_name, columns)
    
    def update(self, obj, table_name, columns, condition):
        """
        Update data in the database based on a condition.
        """
        serialized_obj = pickle.dumps(obj)
        update_query = f"UPDATE {table_name} SET serialized_data = ? WHERE {condition}"
        self.cursor.execute(update_query, (serialized_obj,))
        self.connection.commit()
    
    def delete(self, table_name, condition):
        """
        Delete data from the database based on a condition.
        """
        delete_query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(delete_query)
        self.connection.commit()
    
    def extract(self, table_name):
        """
        Extract data from the specified table.
        """
        return self.deserialize(table_name, [])
