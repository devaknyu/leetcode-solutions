"""
LeetCode 211: Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Problem Description:
- Design a data structure that supports adding new words
  and searching words with wildcard support.
- The search function may contain the '.' character,
  which can represent any single letter.
- Operations required:
  - addWord(word)
  - search(word) with '.' wildcard support

Approach:
- Use a Trie (Prefix Tree) as the underlying data structure.
- Insert words normally character by character.
- For searching:
  - Traverse the trie recursively using DFS.
  - When encountering a '.', try all possible child paths.
  - Continue recursively until the word is fully matched.

Key Observations:
- A Trie efficiently handles prefix-based word storage.
- Wildcard '.' requires branching into multiple paths.
- DFS allows exploration of all valid paths when wildcards appear.
- Worst-case search time increases due to wildcard branching.

Technique: Trie + DFS Backtracking
1. Insert words into the Trie as usual
2. For search:
   - Traverse character by character
   - If character is a letter, move to that child
   - If character is '.', recursively search all children
3. At the end of traversal, check if a word ends at that node

Time Complexity:
- addWord: O(L)
- search:
  - Best case: O(L)
  - Worst case: O(26^L) (when word is all wildcards)
  where L is the word length

Space Complexity:
- O(N), where N is the total number of characters stored
  in the trie
"""

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

# Example usage
if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    print(wd.search("pad"))  # False
    print(wd.search("bad"))  # True
    print(wd.search(".ad"))  # True
    print(wd.search("b.."))  # True
