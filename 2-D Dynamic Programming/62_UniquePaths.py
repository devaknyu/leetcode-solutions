"""
LeetCode 62: Unique Paths
https://leetcode.com/problems/unique-paths/

Approach:
- We are given a grid of size `m x n`.
- A robot starts at the top-left corner and wants to reach the bottom-right corner.
- The robot can only move:
    → Right
    → Down
- The goal is to count the total number of unique paths.

Key Observations:
- At any cell (i, j), the robot can arrive either:
    from the left (i, j-1)
    from above (i-1, j)

So:
    paths[i][j] = paths[i][j+1] + paths[i+1][j]

(when building from bottom-right perspective)

Base Case:
- Last row → only one way (all moves right)
- Last column → only one way (all moves down)

So we initialize:
    row = [1, 1, 1, ..., 1]

Technique: Dynamic Programming (Space Optimized)

Algorithm:
1. Initialize a row of size `n` with all 1s (bottom row)
2. Iterate from bottom to top (m-1 times)
3. For each row:
   - Create a newRow initialized with 1s
   - Traverse from right to left
   - Update:
        newRow[j] = newRow[j+1] + row[j]
4. Update `row = newRow`
5. Return row[0]

Example:

m = 3, n = 3

Start:
row = [1,1,1]

Iteration 1:
newRow = [?, ?, 1]
j=1 → newRow[1] = 1 + 1 = 2
j=0 → newRow[0] = 2 + 1 = 3
row = [3,2,1]

Iteration 2:
newRow = [?, ?, 1]
j=1 → 2 + 1 = 3
j=0 → 3 + 3 = 6
row = [6,3,1]

Result = 6

Technique Insight:
- We reduce 2D DP → 1D DP
- Only previous row is needed

Time Complexity:
- O(m * n)

Space Complexity:
- O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Returns the number of unique paths
        from top-left to bottom-right.
        """

        # Initialize bottom row
        row = [1] * n

        # Build from bottom to top
        for i in range(m - 1):

            newRow = [1] * n

            # Traverse from right to left
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]

            row = newRow

        return row[0]

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (3, 7, 28),
        (3, 3, 6),
        (1, 5, 1),
        (5, 1, 1),
    ]

    for m, n, expected in test_cases:
        result = solution.uniquePaths(m, n)
        status = "✓" if result == expected else "✗"
        print(f"m = {m}, n = {n} → paths = {result} (Expected: {expected}) {status}")

