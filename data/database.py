from pymongo import MongoClient
from typing import Optional
import threading

MONGO_URI = "mongodb://root:admin@mongo:27017/"
DATABASE_NAME = "data_analyzer"
COLLECTION_NAME = "product_reviews"

class MongoDB:
    _instance: Optional["MongoDB"] = None
    _lock = threading.Lock()

    def __init__(self, uri: str = MONGO_URI, db_name: str = DATABASE_NAME):
        if MongoDB._instance is not None:
            raise Exception("Instance is already deployed. Use the `get_instance()` method.")
        
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        MongoDB._instance = self  # Set the singleton instance

    @classmethod
    def get_instance(cls, uri: str = MONGO_URI, db_name: str = DATABASE_NAME) -> "MongoDB":
        """
        Returns the singleton instance of MongoDB client.
        Ensures that only one instance of MongoDB client is created.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = MongoDB(uri, db_name)
        return cls._instance

    def get_collection(self, collection_name: str):
        """Retrieve a MongoDB collection"""
        return self.db[collection_name]

    def close(self):
        """Close the MongoDB client connection"""
        self.client.close()

# Usage example
if __name__ == "__main__":
    # Get MongoDB Singleton instance
    mongo_instance = MongoDB.get_instance(uri="mongodb://localhost:27017/", db_name="test_db")
    collection = mongo_instance.get_collection("test_collection")

    # Insert a document
    collection.insert_one({"name": "Alice", "age": 30})

    # Close the connection
    mongo_instance.close()
