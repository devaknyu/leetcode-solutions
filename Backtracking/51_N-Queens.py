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