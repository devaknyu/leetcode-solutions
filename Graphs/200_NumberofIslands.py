"""
LeetCode 200: Number of Islands
https://leetcode.com/problems/number-of-islands/

Problem Description:
- Given an m x n 2D grid grid representing water ('0') and land ('1'),
  return the number of islands.
- An island is surrounded by water and is formed by connecting adjacent lands
  horizontally or vertically.
- You may assume all four edges of the grid are surrounded by water.

Approach:
- Traverse the grid cell by cell.
- Each time an unvisited land cell ('1') is found, perform a BFS
  to mark the entire island as visited.
- Increment the island count for each BFS traversal.

Key Observations:
- Each island corresponds to exactly one BFS/DFS traversal.
- A visited set prevents revisiting the same land cell.
- BFS explores all connected land cells in four directions.
- Grid traversal ensures every cell is processed at most once.

Technique: Breadth-First Search (BFS on Grid)
1. Iterate through every cell in the grid.
2. When an unvisited land cell is found:
   - Start BFS from that cell.
   - Mark all connected land cells as visited.
   - Increment island count.
3. Continue until the entire grid is processed.

Example:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output:
3

Time Complexity:
- O(m × n)
  - Each cell is visited at most once

Space Complexity:
- O(m × n) in the worst case for the visited set and BFS queue
"""

from typing import List
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        (nr, nc) not in visit and
                        grid[nr][nc] == "1"
                    ):
                        visit.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    island += 1

        return island

if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(Solution().numIslands(grid))