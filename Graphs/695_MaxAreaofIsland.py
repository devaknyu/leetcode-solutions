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