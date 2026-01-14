# Trie node definition
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        """
        Initializes the WordDictionary object.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word exists in the data structure.
        Supports '.' as a wildcard character.
        """

        def dfs(j: int, node: TrieNode) -> bool:
            cur = node

            for i in range(j, len(word)):
                c = word[i]

                # Wildcard case
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                # Normal character case
                if c not in cur.children:
                    return False

                cur = cur.children[c]

            return cur.word

        return dfs(0, self.root)
