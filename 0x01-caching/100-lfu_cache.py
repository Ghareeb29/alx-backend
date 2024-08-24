#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """LFUCache defines:
    - caching system inherit from BaseCaching
    - uses LFU algorithm for cache replacement
    """

    def __init__(self):
        """Initialize LFUCache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = {}

    def __reorder_items(self, mru_key):
        """Reorders items in cache based on frequency and recency"""
        max_freq = max(self.keys_freq.values())
        mru_freq = self.keys_freq[mru_key]
        mru_pos = None
        ins_pos = None
        for i, key in enumerate(self.cache_data):
            if key == mru_key:
                mru_pos = i
                break
            elif self.keys_freq[key] < mru_freq:
                ins_pos = i
        if mru_pos is not None and ins_pos is not None:
            self.cache_data.move_to_end(mru_key, last=False)
            self.cache_data.move_to_end(mru_key, last=(ins_pos == 0))

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys_freq[key] += 1
            self.__reorder_items(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = min(self.keys_freq, key=self.keys_freq.get)
                lfu_keys = [
                    k for k, v in self.keys_freq.items()
                    if v == self.keys_freq[lfu_key]
                ]
                if len(lfu_keys) > 1:
                    for k in self.cache_data:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                del self.cache_data[lfu_key]
                del self.keys_freq[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.keys_freq[key] = 1
            self.__reorder_items(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.keys_freq[key] += 1
            self.__reorder_items(key)
            return self.cache_data[key]
        return None
