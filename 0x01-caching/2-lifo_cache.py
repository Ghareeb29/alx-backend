#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines:
    - caching system inherit from BaseCaching
    - uses LIFO algorithm for cache replacement
    """

    def __init__(self):
        """Initialize LIFOCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded = self.order.pop()
                    del self.cache_data[discarded]
                    print(f"DISCARD: {discarded}")
                else:
                    self.order.remove(key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
