"""
LeetCode 286: Walls and Gates (Islands and Treasure)
https://leetcode.com/problems/walls-and-gates/

Problem Description:
- You are given an m x n grid rooms where:
  - -1 represents a wall
  - 0 represents a gate (treasure)
  - INF (or a large value) represents an empty room
- Fill each empty room with the distance to its nearest gate.
- If it is impossible to reach a gate, leave the room unchanged.
- The grid must be modified in-place.

Approach:
- Use multi-source Breadth-First Search (BFS).
- Treat all gates (0s) as starting points in the BFS.
- Expand outward level by level, updating distances as we go.
- Use a visited set to avoid revisiting cells.

Key Observations:
- BFS guarantees the shortest distance in an unweighted grid.
- Starting BFS from all gates simultaneously ensures each room
  gets the distance to its nearest gate.
- Walls (-1) block traversal.
- Each cell is processed at most once.

Technique: Multi-Source BFS (Grid)
1. Add all gate positions (cells with value 0) to the queue.
2. Mark these positions as visited.
3. Perform BFS level by level:
   - For each cell in the current layer, update its distance.
   - Add all valid neighboring rooms to the queue.
4. Increment distance after finishing each BFS level.

Example:
grid = [
  [INF, -1,  0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0,   -1, INF, INF]
]

Output:
[
  [3, -1, 0, 1],
  [2, 2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]

Time Complexity:
- O(m × n)
  - Each cell is visited at most once

Space Complexity:
- O(m × n)
  - Queue and visited set in the worst case
"""

from typing import List
import collections


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        def addRoom(r, c):
            # Out of bounds, wall, or already visited
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in visit or
                grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        # Initialize BFS with all gates
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1