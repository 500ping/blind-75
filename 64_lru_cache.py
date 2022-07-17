from collections import OrderedDict


class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)



lru = LRUCache(2)
print(lru.put(1, 1))
print(lru.put(2, 2))
print(lru.get(1)   )
print(lru.put(3, 3))
print(lru.get(2)   )
print(lru.put(4, 4))
print(lru.get(1)   )
print(lru.get(3)   )
print(lru.get(4)   )