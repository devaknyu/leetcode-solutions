"""
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