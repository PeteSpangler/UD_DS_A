from collections import OrderedDict

class LRU_Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

        except KeyError:
            return -1

    def put(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity == 0:
            print("No can do, cache is empty")
            return
        
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value

        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value

            else:
                self.cache.popitem(last=False)
                self.cache[key] = value

our_cache = LRU_Cache(5)

our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.put(5, 5) 
our_cache.put(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
