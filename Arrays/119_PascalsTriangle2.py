"""
LeetCode 119: Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Problem:
Given an integer rowIndex, return the rowIndex-th (0-indexed) row of Pascal's triangle.

Example:
Input: rowIndex = 3
Output: [1,3,3,1]

Approach:
- Start with the first row: [1].
- For each new row up to rowIndex:
    - Create a next_row with length len(res) + 1, initialized with 0s.
    - Add each element of the current row to its corresponding position and the next position in next_row.
    - Assign next_row to res.
- Return the final res.

Time Complexity: O(rowIndex^2)
    - Each row i has i+1 elements, so total operations sum up to ~rowIndex^2/2.
Space Complexity: O(rowIndex)
    - We only store the current row at any time.
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row
        return res
    
    # Example run for local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.getRow(3))  # Expected [1, 3, 3, 1]