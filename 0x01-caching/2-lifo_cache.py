#!/usr/bin/python3
"""LIFO caching module"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache with the given key,
        replacing the existing value if it already exists.

        Args:
            key (Any): The key to associate the item with.
            item (Any): The item to store in the cache.

        Returns:
            None

        Prints:
            - "DISCARD: {Discarded}" if the cache is full and
            an item needs to be discarded to make space for the new item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                Discarded = next(reversed(self.cache_data))
                del self.cache_data[Discarded]
                print("DISCARD: {}".format(Discarded))

    def get(self, key):
        """
        Retrieves an item from the cache based on the provided key.

        Args:
            key (Any): The key used to identify the item in the cache.

        Returns:
            Any or None: The item associated with the key
            if it exists in the cache, otherwise None.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
