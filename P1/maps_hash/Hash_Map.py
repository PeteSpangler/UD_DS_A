class HashMap:
    
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37                  # a prime numbers 
        self.num_entries = 0
        
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    # Returns the bucket_index
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)        #the returned hash code will be the bucket_index
        return bucket_index
    
    
    # Returns the hash code
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)                          # length of array to be used in Mod operation
        
        current_coefficient = 1                                       # represents (self.p^0) which is 1
        
        hash_code = 0
        
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code (Mod operation)
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient as well

        return hash_code % num_buckets                                # one last compression before returninghash_map = HashMap()