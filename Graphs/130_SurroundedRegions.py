"""
LeetCode 130: Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Approach:
- Any 'O' completely surrounded by 'X' should be flipped
- 'O's connected to the border can never be surrounded
- First, mark all border-connected 'O's as temporary ('T')
- Then flip all remaining 'O's to 'X'
- Finally, convert temporary marks back to 'O'

Technique: Reverse DFS from Boundary
1. Traverse all boundary cells
2. When a boundary 'O' is found, DFS to mark all connected 'O's as 'T'
3. After DFS, all unmarked 'O's are fully surrounded → flip to 'X'
4. Restore all 'T's back to 'O'

Time Complexity: O(m * n)
- Each cell is visited at most once

Space Complexity: O(m * n)
- Recursion stack in the worst case
"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Capture all border-connected regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (
                    r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1
                ):
                    capture(r, c)

        # Step 2: Flip all surrounded 'O' to 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Step 3: Restore non-surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

# Example usage
if __name__ == "__main__":
    sol = Solution()

    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]

    print("Before:")
    for row in board:
        print(row)

    sol.solve(board)

    print("\nAfter:")
    for row in board:
        print(row)