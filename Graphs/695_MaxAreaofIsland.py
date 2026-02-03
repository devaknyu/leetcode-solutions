"""
LeetCode 695: Max Area of Island
https://leetcode.com/problems/max-area-of-island/

Problem Description:
- Given an m x n binary grid grid where:
  - 1 represents land
  - 0 represents water
- An island is formed by connecting adjacent lands
  horizontally or vertically.
- Return the maximum area of an island in the grid.
- If there is no island, return 0.

Approach:
- Use Depth-First Search (DFS) to explore each island.
- For every unvisited land cell, run DFS to compute
  the total area of that island.
- Track the maximum area encountered.

Key Observations:
- Each land cell is visited exactly once.
- DFS naturally accumulates area by counting connected cells.
- A visited set prevents recounting the same cell.
- The DFS returns the area contribution of the current cell.

Technique: Depth-First Search (DFS on Grid)
1. Traverse every cell in the grid.
2. When an unvisited land cell is found:
   - Start DFS and compute the area of the island.
3. DFS rules:
   - Stop if out of bounds, water, or already visited.
   - Count the current cell and explore neighbors.
4. Update the maximum area after each DFS.

Example:
grid = [
  [0,0,1,0,0],
  [0,1,1,1,0],
  [0,0,1,0,0],
  [1,1,0,0,0]
]

Output:
5

Time Complexity:
- O(m × n)
  - Each cell is visited at most once

Space Complexity:
- O(m × n) in the worst case for recursion stack and visited set
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # Out of bounds, water, or already visited
            if (
                r < 0 or r == rows or
                c < 0 or c == cols or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0

            visited.add((r, c))

            # Count current cell + neighbors
            return (
                1 +
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))

        return area

if __name__ == "__main__":
    grid = [
        [0,0,1,0,0],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [1,1,0,0,0]
    ]
    print(Solution().maxAreaOfIsland(grid))