"""
LeetCode 208: Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Problem Description:
- Implement a Trie (Prefix Tree) with the following operations:
  - insert(word): Inserts a word into the trie.
  - search(word): Returns True if the word exists in the trie.
  - startsWith(prefix): Returns True if there is any word
    in the trie that starts with the given prefix.

Approach:
- Use a tree-like data structure where:
  - Each node represents a character.
  - Each node maintains a map of child characters.
  - A boolean flag marks whether a complete word ends at that node.
- Traverse character by character for each operation.

Key Observations:
- Trie efficiently supports prefix-based queries.
- Insert and search operations run in linear time
  relative to the length of the word.
- A word may exist as a prefix without being a complete word.
- The end-of-word flag distinguishes full words from prefixes.

Technique: Trie / Prefix Tree
1. Initialize a root node with empty children
2. For insertion:
   - Traverse characters, creating nodes as needed
   - Mark the last node as end-of-word
3. For search:
   - Traverse characters
   - Ensure end-of-word is True at the final node
4. For prefix check:
   - Traverse characters without checking end-of-word

Time Complexity:
- insert: O(L)
- search: O(L)
- startsWith: O(L)
  where L is the length of the word or prefix

Space Complexity:
- O(N), where N is the total number of characters stored
  in the trie
"""

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

# Example usage
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

    print(trie.search("apple"))    # True
    print(trie.search("app"))      # False
    print(trie.startsWith("app"))  # True

    trie.insert("app")
    print(trie.search("app"))      # True