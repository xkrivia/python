# CHRIS FELLI, 2019
# Design an LRU Cache
# It should support the following operations: get and put.
# 1) get(key) - Get the value (will always be positive) of the key 
# if the key exists in the cache, otherwise return -1.
# 2) put(key, value) - Set or insert the value if the key is not 
# already present. When the cache reached its capacity, it should
# invalidate the least recently used item before inserting a new item.
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict

class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key) -> int:
        if key not in self.cache: 
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

# Testcases
test = LRUCache(2)
test.put(1, 1)
test.put(1, 1)
test.put(2, 2)
print(test.get(1))
test.put(3, 3)
print(test.get(2))
test.put(4, 4)
print(test.get(1))
print(test.get(3))
print(test.get(4))