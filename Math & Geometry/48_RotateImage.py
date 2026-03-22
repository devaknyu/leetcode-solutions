"""
LeetCode 48: Rotate Image
https://leetcode.com/problems/rotate-image/

Approach:
- We are given an n x n 2D matrix representing an image.
- The goal is to rotate the image by 90 degrees clockwise.
- The rotation must be done **in-place** (no extra matrix).

Key Observations:
- Rotation happens layer by layer (like peeling an onion).
- Each layer is bounded by left (l) and right (r) pointers.
- For each layer, we perform a **4-way swap**:
    top ← left ← bottom ← right ← top

Visual Mapping:

Before Rotation (indices):
(top, left+i)          (top+i, right)
        →        ↓
(bottom-i, left)   ←   (bottom, right-i)

Each group of 4 elements rotates cyclically.

Example:

matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

After rotation:
[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]

Technique: Matrix Manipulation (Layer-by-Layer Rotation)

Algorithm:
1. Initialize two pointers:
   - l = 0 (left boundary)
   - r = n - 1 (right boundary)

2. While l < r:
   - Iterate through elements in current layer
   - For each index i:
       a. Save top-left value
       b. Move bottom-left → top-left
       c. Move bottom-right → bottom-left
       d. Move top-right → bottom-right
       e. Move saved top-left → top-right

3. Move inward:
   - l += 1
   - r -= 1

4. Repeat until all layers are processed

Time Complexity:
- Each element is visited once
- Time Complexity: O(n^2)

Space Complexity:
- In-place rotation
- Space Complexity: O(1)
"""

class Solution:
    def rotate(self, matrix):
        """
        Rotates the matrix 90 degrees clockwise in-place.
        """

        l, r = 0, len(matrix) - 1

        while l < r:

            for i in range(r - l):

                top, bottom = l, r

                # Save top-left
                topLeft = matrix[top][l + i]

                # Move bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top-left → top-right
                matrix[top + i][r] = topLeft

            # Move inward
            l += 1
            r -= 1

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]],
         [[7,4,1],[8,5,2],[9,6,3]]),

        ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
         [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
    ]

    for matrix, expected in test_cases:
        original = [row[:] for row in matrix]  # copy for display
        solution.rotate(matrix)
        status = "✓" if matrix == expected else "✗"
        print(f"matrix = {original} → rotated = {matrix} (Expected: {expected}) {status}")