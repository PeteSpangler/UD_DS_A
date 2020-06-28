import hashlib
import datetime
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode("utf-8")
      sha.update(hash_str)
      return sha.hexdigest()

def get_utc_time():
      utc = datetime.datetime.utcnow()
      return utc.strftime("%d/%m/%Y %H:%M:%S")

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp = self.last
            self.last = Block(timestamp, data, temp)
            self.last.previous_hash = temp



blockA = Block(get_utc_time(), "Michael Jordan", 0)
blockB = Block(get_utc_time(), "Is the", blockA)
blockC = Block(get_utc_time(), "GOAT", blockB)

print(blockA.data)
print(blockA.hash)
print(blockA.timestamp)
print(blockB.data)
print(blockC.data)

temp = LinkedList()
temp.append(get_utc_time(), "or anyone else")
temp.append(get_utc_time(), "not Lebron")
print(temp.last.data)
print(temp.last.previous_hash.data)