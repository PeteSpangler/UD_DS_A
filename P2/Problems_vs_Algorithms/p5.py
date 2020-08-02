## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
        
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
     
    def suffixes(self, suffix = ""):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        xes = []

        for char in self.children:
            if self.children[char].is_word:
                xes.append(suffix+char)
            xes += self.children[char].suffixes(suffix+char)
        return xes
    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        
    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None   
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

#To avoid returing full wordlist when running tests
def findit(prefix):
    if prefix == "":
        print([])
    if prefix != "":
        pnode = MyTrie.find(prefix)
        if pnode:
            print(pnode.suffixes())

#Tests
print(findit("tr"))
print(findit("an"))
print(findit("f"))
print(findit(""))
print(findit("fun"))