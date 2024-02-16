import sqlite3
import pickle

from typing import Any, Dict, List, Tuple

from abc import ABC, abstractmethod

class Serializable(ABC):
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """
        Create a table in the database.
        """
        column_definitions = ', '.join([f"{column} TEXT" for column in columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(create_table_query)
        self.connection.commit()
    
    def serialize(self, table_name, columns, obj=None):
        """
        Serialize an object and insert it into the database.
        """
        if obj is None:
            obj = self
            self.create_table(table_name, columns)
            obj_dict = self.__dict__.copy()
            obj_dict.pop('db_name', None)
            obj_dict.pop('connection', None)
            obj_dict.pop('cursor', None)
            obj_dict.pop('db', None)
            values = [obj_dict.get(column) for column in columns]
            placeholders = ', '.join(['?' for _ in columns])
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(values))
            self.connection.commit()
        else:
            self.create_table(table_name, columns)
            placeholders = ', '.join(['?' for _ in columns])
            for data in obj:
                self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
            self.connection.commit()


    def deserialize(self, table_name, columns):
        """
        Deserialize an object from the database.
        """
        self.create_table(table_name, columns)
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        deserialized_objs = []
        for row in rows:
            deserialized_objs.append(pickle.loads(row[0]))
        return deserialized_objs

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()
