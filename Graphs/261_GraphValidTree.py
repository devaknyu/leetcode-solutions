"""
LeetCode 261: Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

Approach:
- A valid tree must satisfy TWO conditions:
  1) No cycles
  2) Fully connected (all nodes reachable)
- Since the graph is undirected, we use DFS with a `prev` parameter
  to avoid treating the parent edge as a cycle
- After DFS, verify that all nodes were visited

Technique: DFS Cycle Detection in Undirected Graph
1. Build adjacency list for the undirected graph
2. Use DFS starting from node 0
3. Track visited nodes
4. If we revisit a node (excluding parent), a cycle exists
5. After DFS, ensure all nodes were visited (connected)

Time Complexity: O(V + E)
- V = number of nodes
- E = number of edges

Space Complexity: O(V + E)
- Adjacency list + recursion stack + visited set
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        # Must have no cycles AND be fully connected
        return dfs(0, -1) and n == len(visit)

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (5, [[0,1],[0,2],[0,3],[1,4]]),        # True
        (5, [[0,1],[1,2],[2,3],[1,3],[1,4]]),  # False (cycle)
        (4, [[0,1],[2,3]]),                    # False (disconnected)
    ]

    for n, edges in test_cases:
        result = sol.validTree(n, edges)
        print(f"n={n}, edges={edges}")
        print(f"Output: {result}\n")