"""
LeetCode 212: Word Search II
https://leetcode.com/problems/word-search-ii/

Problem Description:
- Given a 2D board of characters and a list of words,
  return all words that can be formed by sequentially adjacent cells.
- Adjacent cells are horizontally or vertically neighboring.
- The same letter cell may not be used more than once per word.

Approach:
- Use a Trie to efficiently store all target words.
- Perform DFS backtracking from each cell in the board.
- Traverse the Trie simultaneously while exploring the board.
- Stop exploring paths that do not match any Trie prefix.

Key Observations:
- Naively checking each word separately is inefficient.
- Trie enables prefix pruning to drastically reduce search space.
- DFS + backtracking ensures valid path construction.
- Using a set avoids duplicate results.

Technique: Trie + DFS Backtracking
1. Insert all words into a Trie
2. For each board cell:
   - Start DFS if the character exists in Trie root
3. During DFS:
   - Check board bounds and visited cells
   - Move through Trie children based on board characters
   - Track visited cells to prevent reuse
4. When reaching end-of-word, add result
5. Backtrack by unmarking visited cells

Time Complexity:
- O(m × n × 4^L) in the worst case,
  where:
  - m × n is the board size
  - L is the maximum word length

Space Complexity:
- O(N), where N is the total number of characters
  stored in the Trie
- Additional O(L) recursion stack for DFS
"""

from typing import List

# Trie node definition
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Returns all words found in the board.
        """

        # Build Trie
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROW, COL = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r: int, c: int, node: TrieNode, word: str) -> None:
            # Boundary and pruning checks
            if (
                r < 0 or c < 0 or
                r == ROW or c == COL or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            # Found a complete word
            if node.endofword:
                res.add(word)

            # Explore neighbors
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack
            visit.remove((r, c))

        # Start DFS from every board cell
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, root, "")

        return list(res)

# Example usage
if __name__ == "__main__":
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]

    print(Solution().findWords(board, words))
    # Expected: ["oath", "eat"]