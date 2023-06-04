from collections import deque


class LRUCache:
    """
    LRU Cache model implementation
    """

    def __init__(self, size: int = 1000):
        """
        initialize the LRUCache

        Args:
            size (int): The maximum size of the cache, default 1000
        """
        self.data = {}
        self.max_size = size
        self.order = deque(maxlen=size)

    def put(self, key: str, value: any) -> None:
        """
        insert a key-value pair into the cache
        if the key already exists, the previous value is updated
        if the cache is full, the least recently used item is removed

        Args:
            key (str): The key
            value (any): The value associated with the key
        """
        if key in self.data:
            self.order.remove(key)
            del self.data[key]

        if len(self.data) == self.max_size:
            self.pop_least_recently_used()

        self.data[key] = value
        self.order.append(key)
        print(self.data)

    def pop_least_recently_used(self) -> None:
        """
        remove the least recently used item from the cache
        """
        if len(self.data) != 0:
            key = self.order.popleft()
            del self.data[key]

    def get(self, key: str) -> any:
        """
        retrieve the value associated with a key from the cache
        if the key is found, it's considered the most recently used item so the order is updated accordingly

        Args:
            key (str): The key to search for
        Returns:
            any: The value associated with the key, or None if the key is not found
        """
        print(self.data)
        if key in self.data:
            self.order.remove(key)
            self.order.append(key)
            return self.data[key]
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
