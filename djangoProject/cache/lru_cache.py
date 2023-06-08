from pymongo import MongoClient
from djangoProject.database_with_mongodb.apps import DatabaseWithMongodbConfig


class LRUCache:
    """
    LRU Cache model implementation using MongoDB
    """

    def __init__(self, size: int = 1000):
        """
        Initialize the LRUCache

        Args:
            size (int): The maximum size of the cache, default 1000
        """
        self.db_handle = DatabaseWithMongodbConfig.db_handle
        self.client = DatabaseWithMongodbConfig.client
        self.db = self.client["cache_db"]
        self.collection = self.db["cache_data"]
        self.collection.create_index([("key", 1)], unique=True)
        self.max_size = size

    def put(self, key: str, value: any) -> None:
        """
        Insert a key-value pair into the cache.
        If the key already exists, the previous value is updated.
        If the cache is full, the least recently used item is removed.

        Args:
            key (str): The key
            value (any): The value associated with the key
        """
        if key in self.collection.distinct("key"):
            self.collection.delete_one({"key": key})

        if self.collection.count_documents({}) == self.max_size:
            self.pop_least_recently_used()

        self.collection.insert_one({"key": key, "value": value})

    def pop_least_recently_used(self) -> None:
        """
        Remove the least recently used item from the cache.
        """
        document = self.collection.find_one_and_delete({}, sort=[("_id", 1)])
        if document:
            print("Removing item:", document)

    def get(self, key: str) -> any:
        """
        Retrieve the value associated with a key from the cache.
        If the key is found, it's considered the most recently used item so the order is updated accordingly.

        Args:
            key (str): The key to search for
        Returns:
            any: The value associated with the key, or None if the key is not found
        """
        document = self.collection.find_one_and_update(
            {"key": key},
            {"$currentDate": {"lastAccessed": True}},
            return_document=True,
        )
        if document:
            print("GET from Cache")
            print("Retrieving item:", document)
            return document["value"]
        return None


class AppCache:
    """
    Singleton class to create an instance of LRUCache
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, size: int = 1000):
        if not hasattr(self, "cache_instance"):
            self.cache_instance = LRUCache(size)
