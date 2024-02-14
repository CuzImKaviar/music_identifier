import sqlite3
from abc import ABC, abstractmethod

class Serializable(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def get_db_connector(self):
        return None

    def store(self):
        print("Storing data...")
