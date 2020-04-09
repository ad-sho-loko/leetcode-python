class Trie:

    def __init__(self):
        self.top = {}

    def insert(self, word: str) -> None:
        n = self.top
        for ch in word:
            if ch not in n.keys():
                n[ch] = {}

            n = n[ch]

        n["_"] = {}

    def search(self, word: str) -> bool:
        n = self.top
        for ch in word:
            if ch not in n.keys():
                return False

            n = n[ch]

        return "_" in n.keys()

    def startsWith(self, prefix: str) -> bool:
        n = self.top
        for ch in prefix:
            if ch not in n.keys():
                return False

            n = n[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
