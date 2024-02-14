import sqlite3
from datetime import datetime
from abc import ABC, abstractmethod

class Serializable(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def get_db_connector(self):
        return None
    
    def store(self):
        print("Storing data...")

        conn = self.get_db_connector()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM songs WHERE id=?", (self.id,))
        result = cursor.fetchone()

        if result:
                # Update the existing record with the current instance's data
                cursor.execute("UPDATE songs SET column1=?, column2=?, ... WHERE id=?", (self.attribute1, self.attribute2, ..., self.id))
                print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            cursor.execute("INSERT INTO songs (id, column1, column2, ...) VALUES (?, ?, ?, ...)", (self.id, self.attribute1, self.attribute2, ...))
            print("Data inserted.")

        conn.commit()
        conn.close()
    
    def delete(self):
        conn = self.get_db_connector()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM songs WHERE id=?", (self.id,))
        print("Data deleted.")

        conn.commit()
        conn.close()

    @abstractmethod
    def to_dict(self):
        pass
