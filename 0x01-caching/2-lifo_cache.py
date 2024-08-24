#!/usr/bin/python3
"""LIFO caching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using LIFO algorithm.

        If the cache is at capacity, remove the most recently added item
        before adding the new item. If key or item is None, this method
        should not do anything.

        Args:
        key: The key to store the item under.
        item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                discarded = self.order.pop()
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

        if key in self.cache_data:
            self.order.remove(key)

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
        key: The key of the item to retrieve.

        Returns:
        The value associated with the key if it exists, None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
