"""
LeetCode 54: Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Approach:
- We are given an m x n matrix.
- The goal is to return all elements in **spiral order**.

Spiral traversal order:
→ left to right (top row)
↓ top to bottom (right column)
← right to left (bottom row)
↑ bottom to top (left column)

Repeat while shrinking boundaries.

Key Observations:
- We maintain four boundaries:
    l (left), r (right)
    top, bottom

- After traversing one side, we shrink the corresponding boundary.
- We must check boundaries carefully to avoid duplicate traversals.

Example:

matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

Spiral Order:
[1,2,3,6,9,8,7,4,5]

Technique: Matrix Traversal (Boundary Simulation)

Algorithm:
1. Initialize:
   - l = 0, r = number of columns
   - top = 0, bottom = number of rows
   - result list

2. While l < r and top < bottom:
   a. Traverse top row (left → right)
   b. Move top boundary down

   c. Traverse right column (top → bottom)
   d. Move right boundary left

   e. Check if boundaries still valid

   f. Traverse bottom row (right → left)
   g. Move bottom boundary up

   h. Traverse left column (bottom → top)
   i. Move left boundary right

3. Return result

Why boundary check is needed:
- Prevents re-traversing rows/columns in single row/column cases

Time Complexity:
- Each element is visited once
- Time Complexity: O(m * n)

Space Complexity:
- Output list
- Space Complexity: O(1) extra (excluding result)
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        Returns elements of the matrix in spiral order.
        """

        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        res = []

        while l < r and top < bottom:

            # Traverse top row
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            # Traverse right column
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1

            # Check boundaries before continuing
            if not (l < r and top < bottom):
                break

            # Traverse bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]],
         [1,2,3,6,9,8,7,4,5]),

        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]],
         [1,2,3,4,8,12,11,10,9,5,6,7]),

        ([[1]],
         [1]),
    ]

    for matrix, expected in test_cases:
        result = solution.spiralOrder(matrix)
        status = "✓" if result == expected else "✗"
        print(f"matrix = {matrix} → spiral = {result} (Expected: {expected}) {status}")