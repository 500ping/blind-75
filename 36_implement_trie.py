class Trie:

    def __init__(self):
        self.data = []        

    def insert(self, word: str) -> None:
        self.data.append(word)

    def search(self, word: str) -> bool:
        return word in self.data

    def startsWith(self, prefix: str) -> bool:
        for word in self.data:
            if word.startswith(prefix):
                return True
        return False


trie = Trie()
trie.insert("apple")
trie.search("apple")   
trie.search("app")     
trie.startsWith("app") 
trie.insert("app")
trie.search("app")     