"""
LeetCode 79: Word Search
https://leetcode.com/problems/word-search/

Problem Description:
- Given an m x n grid of characters board and a string word,
  return true if word exists in the grid.
- The word must be constructed from sequentially adjacent cells
  (horizontally or vertically).
- The same cell may not be used more than once in a single word path.

Approach:
- Use Depth-First Search (DFS) with backtracking.
- Try to start the word from every cell in the grid.
- From each cell, explore all four directions (up, down, left, right).
- Use a set to track the current path (visited cells).

Key Observations:
- Backtracking is required because cells cannot be reused.
- As soon as a character does not match, stop exploring that path.
- If all characters of the word are matched, return true immediately.
- Early termination greatly reduces unnecessary exploration.

Technique: Backtracking (DFS on Grid)
1. Iterate through each cell in the grid as a starting point.
2. For each cell, run DFS with the current word index.
3. In DFS:
   - If index equals word length → word is found.
   - If out of bounds, character mismatch, or cell already visited → stop.
   - Mark the cell as visited and explore neighbors.
4. Backtrack by unmarking the cell after exploration.

Example:
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

Output:
True

Time Complexity:
- O(m × n × 4ˡ)
  - m × n possible starting cells
  - 4 choices per character (up to length l of word)

Space Complexity:
- O(l) for recursion depth
- O(l) for visited path storage
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # All characters matched
            if i == len(word):
                return True

            # Out of bounds, mismatch, or already visited
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in path
            ):
                return False

            # Mark current cell as visited
            path.add((r, c))

            # Explore all four directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Backtrack
            path.remove((r, c))
            return found

        # Try starting DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

if __name__ == "__main__":
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))