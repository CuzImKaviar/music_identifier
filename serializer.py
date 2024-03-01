import sqlite3
from typing import Any, Dict, List, Tuple
from abc import ABC, abstractmethod

class Serializable(ABC):
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, values: Tuple[Any, ...] = None) -> List[Tuple]:
        """
        Execute a query and return the results.
        """
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_table(self, table_name, columns):
        """
        Create a table in the database.
        """
        table_name = table_name.replace(' ', '_').replace('(', '_').replace(')', '_')
        column_definitions = ', '.join([f"{column}" for column in columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(create_table_query)
        self.connection.commit()
    
    def remove_table(self, table_name):
        """
        Remove a table from the database.
        """
        table_name = table_name.replace(' ', '_').replace('(', '_').replace(')', '_')
        remove_table_query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(remove_table_query)
        self.connection.commit()

    def delete_entry(self, table_name, column, value):
        """
        Delete an object from the database.
        """
        table_name = table_name.replace(' ', '_').replace('(', '_').replace(')', '_')
        delete_query = f"DELETE FROM {table_name} WHERE {column} = ?"
        self.cursor.execute(delete_query, (value,))
        self.connection.commit()
    
    def serialize(self, table_name, columns, a_list=None):
        """
        Serialize an object and insert it into the database.
        """
        if a_list is None:
            table_name = table_name.replace(' ', '_').replace('(', '_').replace(')', '_')
            self.create_table(table_name, columns)    
            values = [self.__dict__.get(column) for column in columns]
            placeholders = ', '.join(['?' for _ in columns])
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(values))
            self.connection.commit()
        else:
            table_name = table_name.replace(' ', '_').replace('(', '_').replace(')', '_')
            self.create_table(table_name, columns)
            placeholders = ', '.join(['?' for _ in columns])
            self.cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", a_list)
            self.connection.commit()

    def deserialize(self, table_name, columns):
        """
        Deserialize an object from the database.
        """
        table_name = table_name.replace(' ', '_').replace('(', '_').replace(')', '_')
        columns_str = ', '.join(columns)
        self.cursor.execute(f"SELECT {columns_str} FROM {table_name}")
        rows = self.cursor.fetchall()
        deserialized_objs = []
        for row in rows:
            obj_dict = {column: value for column, value in zip(columns, row)}
            deserialized_objs.append(obj_dict)
        return deserialized_objs

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()