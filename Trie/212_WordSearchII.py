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
