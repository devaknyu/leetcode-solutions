"""
LeetCode 684: Redundant Connection
https://leetcode.com/problems/redundant-connection/

Approach:
- The graph started as a tree (n nodes, n-1 edges)
- One extra edge was added, creating exactly one cycle
- We must return the edge that creates the cycle
- Use Union-Find to detect when two nodes are already connected

Technique: Union-Find (Cycle Detection in Undirected Graph)
1. Initialize each node as its own parent
2. For each edge:
   - If both nodes already share the same parent → cycle found
   - Otherwise, union them
3. The first edge that fails union is the redundant edge

Time Complexity: O(N * α(N))
- Nearly linear time
- α(N) = inverse Ackermann (almost constant)

Space Complexity: O(N)
- Parent and rank arrays
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        # Parent and rank initialization
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n1):
            # Path Compression
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # Cycle detected
            if p1 == p2:
                return False

            # Union by Rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [[1,2],[1,3],[2,3]],              # → [2,3]
        [[1,2],[2,3],[3,4],[1,4],[1,5]],  # → [1,4]
    ]

    for edges in test_cases:
        result = sol.findRedundantConnection(edges)
        print(f"edges={edges}")
        print(f"Output: {result}\n")