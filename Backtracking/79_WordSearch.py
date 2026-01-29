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