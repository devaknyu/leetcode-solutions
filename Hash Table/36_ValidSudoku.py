"""
LeetCode 36: Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Approach:
- Check if 9x9 Sudoku board is valid (no duplicates in rows, columns, or 3x3 sub-boxes)
- Don't need to solve, only validate existing numbers
- Use sets to track seen numbers in rows, columns, and sub-boxes

Technique: Hash Sets for Rows, Columns, and Sub-boxes
1. Track numbers in each row using dictionary of sets
2. Track numbers in each column using dictionary of sets  
3. Track numbers in each 3x3 sub-box using (r//3, c//3) as key
4. Return false if any duplicate found

Time Complexity: O(1) - fixed 81 cells to check
Space Complexity: O(1) - fixed storage for 9 rows, 9 cols, 9 boxes
"""

import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # Check if number already exists in current row, column or 3x3 box
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                # Add to tracking sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                
        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_boards = [
        # Valid board
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        # Invalid board - duplicate in first row
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    ]
    
    for i, board in enumerate(test_boards):
        result = sol.isValidSudoku(board)
        print(f"Board {i+1}: {'Valid' if result else 'Invalid'}")