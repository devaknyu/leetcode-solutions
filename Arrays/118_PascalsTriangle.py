"""
LeetCode 118: Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Problem:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: numRows = 5
Output:
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]

Approach (using padding with zeros):
- Start with the first row: [1].
- For each new row:
    - Take the previous row, pad it with 0 at both ends.
    - Add adjacent pairs to form the next row.
- Append the row to the result.

Time Complexity: O(numRows^2)
    - We build each row, each with up to numRows elements.
Space Complexity: O(numRows^2)
    - We store all rows in the triangle.
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]   # pad with zeros
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
    
    # Example run for local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))  # Expected [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]