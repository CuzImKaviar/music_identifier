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
        column_definitions = ', '.join([f"{column} TEXT" for column in columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(create_table_query)
        self.connection.commit()
    
    def serialize(self, obj, table_name, columns):
        self.create_table(table_name, columns)
        serialized_obj = pickle.dumps(obj)
        self.cursor.execute(f"INSERT INTO {table_name} VALUES (?)", (serialized_obj,))
        self.connection.commit()

    def deserialize(self, table_name, columns):
        self.create_table(table_name, columns)
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        deserialized_objs = []
        for row in rows:
            deserialized_objs.append(pickle.loads(row[0]))
        return deserialized_objs

    def close(self):
        self.connection.close()
