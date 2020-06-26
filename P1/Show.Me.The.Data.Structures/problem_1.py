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

test_cache = LRU_Cache(5)

test_cache.put(1, 1)
test_cache.put(2, 2)
test_cache.put(3, 3)
test_cache.put(4, 4)


print(test_cache.get(1))       # returns 1
print(test_cache.get(2))       # returns 2
print(test_cache.get(9))       # returns -1 because 9 is not present in the cache
#edge cases
new_cache = LRU_Cache(0)
new_cache.put(1, 1) # returns "No can do, cache is empty"
big_cache = LRU_Cache(100) #Large number case
big_cache.put(1, 1)
big_cache.put(3, 3)
big_cache.put(2, 2)
big_cache.put(99, 99)
print(big_cache.get(99))