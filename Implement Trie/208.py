class TrieNode:
    def __init__(self):
        self.edges = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.edges:
                current.edges[c] = TrieNode()
            current = current.edges[c]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.edges:
                return False
            current = current.edges[c]
        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c not in current.edges:
                return False
            current = current.edges[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)