# Trie node definition
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:
    def __init__(self):
        """
        Initializes the Trie object.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endofword = True

    def search(self, word: str) -> bool:
        """
        Returns True if the exact word exists in the trie.
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endofword

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if any word in the trie starts with the given prefix.
        """
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True