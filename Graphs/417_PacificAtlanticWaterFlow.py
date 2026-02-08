"""
LeetCode 417: Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

Approach:
- Instead of simulating water flowing from every cell to the oceans,
  reverse the logic and simulate flow *from the oceans inward*
- A cell can reach an ocean if water can flow from that ocean to the cell
- Perform DFS from Pacific-border cells and Atlantic-border cells
- Cells reachable from both oceans are part of the answer

Technique: Reverse DFS from Multiple Sources
1. Create two visited sets: pacific-reachable and atlantic-reachable
2. Start DFS from all Pacific-border cells (top row, left column)
3. Start DFS from all Atlantic-border cells (bottom row, right column)
4. During DFS, only move to neighbors with height >= previous cell
   (reverse of water flowing downhill)
5. Intersection of both visited sets gives the result

Time Complexity: O(m * n)
- Each cell is visited at most once for Pacific and once for Atlantic

Space Complexity: O(m * n)
- Visited sets + recursion stack
"""

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # DFS from Pacific Ocean borders (top row, left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # DFS from Atlantic Ocean borders (bottom row, right column)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Cells reachable by both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
    
    # Example usage
if __name__ == "__main__":
    sol = Solution()
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    print(sol.pacificAtlantic(heights))