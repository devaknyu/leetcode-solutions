"""
LeetCode 51: N-Queens
https://leetcode.com/problems/n-queens/

Problem Description:
- The n-queens puzzle is the problem of placing n queens on an n×n chessboard
  such that no two queens attack each other.
- A queen can attack another queen if they share the same row, column,
  or diagonal.
- Return all distinct solutions to the n-queens puzzle.
- Each solution contains a board configuration represented as strings.

Approach:
- Use backtracking by placing one queen per row.
- Track conflicts using three sets:
  - col: columns that already contain a queen
  - posDiag: positive diagonals (r + c)
  - negDiag: negative diagonals (r - c)
- Maintain a board to construct the visual representation.

Key Observations:
- Only one queen is placed per row → no need to track rows.
- Column and diagonal conflicts can be checked in O(1) using sets.
- Backtracking removes the queen after exploring each possibility.
- Valid boards are recorded only when all rows are filled.

Technique: Backtracking (DFS with Constraints)
1. Start from row 0.
2. For each column in the current row:
   - Skip if the column or diagonals are under attack.
3. Place the queen and mark its column and diagonals.
4. Recursively process the next row.
5. When row == n, record the board.
6. Backtrack by removing the queen and unmarking constraints.

Example:
n = 4

Solutions:
[
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]

Time Complexity:
- O(n!) in the worst case
- Pruning via column and diagonal checks reduces the search space

Space Complexity:
- O(n) for recursion depth
- O(n) for sets tracking columns and diagonals
- O(n²) for board representation
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set()  # r + c
        negDiag = set()  # r - c

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # All queens placed successfully
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # Check column and diagonal conflicts
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Backtrack
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

if __name__ == "__main__":
    n = 4
    print(Solution().solveNQueens(n))