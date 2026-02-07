"""
LeetCode 994: Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

Approach:
- Use Breadth-First Search (BFS) to simulate the rotting process minute by minute
- Treat all initially rotten oranges as starting points (multi-source BFS)
- Each BFS level represents one unit of time
- Fresh oranges adjacent to rotten ones become rotten

Technique: Multi-Source BFS (Level Order Traversal)
1. Count all fresh oranges and enqueue all rotten oranges initially
2. Perform BFS layer by layer (each layer = 1 minute)
3. For each rotten orange, rot its 4-directionally adjacent fresh neighbors
4. Decrease fresh count as oranges rot
5. If all fresh oranges rot, return time; otherwise return -1

Time Complexity: O(m * n)
- Each cell is processed at most once

Space Complexity: O(m * n)
- Queue can hold all cells in the worst case
"""

from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])

        # Initialize fresh count and queue with all rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # BFS traversal
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row < 0 or row >= ROWS or
                        col < 0 or col >= COLS or
                        grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[2,1,1],[1,1,0],[0,1,1]], 4),
        ([[2,1,1],[0,1,1],[1,0,1]], -1),
        ([[0,2]], 0),
    ]

    for grid, expected in test_cases:
        print(f"Output: {sol.orangesRotting(grid)} | Expected: {expected}")