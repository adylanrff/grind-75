from collections import defaultdict


class Trie:

    def __init__(self):
        self.children = {}  # dict of trie nodes
        self.is_end = False

    def insert(self, word: str) -> None:
        current_node = self
        for ch in word:
            if not current_node.children.get(ch):
                current_node.children[ch] = Trie()

            current_node = current_node.children.get(ch)
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self
        for ch in word:
            if not current_node.children.get(ch):
                return False
            current_node = current_node.children.get(ch)

        if current_node.is_end:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self
        for ch in prefix:
            if not current_node.children.get(ch):
                return False
            current_node = current_node.children.get(ch)

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
