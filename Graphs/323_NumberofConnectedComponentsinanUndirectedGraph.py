"""
LeetCode 323: Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Approach:
- Initially, each node is its own connected component
- Use Union-Find (Disjoint Set Union) to merge connected nodes
- Every successful union reduces the number of components by 1
- Final count represents total connected components

Technique: Union-Find (Path Compression + Union by Rank)
1. Initialize each node as its own parent
2. For each edge, union the two nodes
3. If union succeeds (different parents), decrease component count
4. Return remaining component count

Time Complexity: O(E * α(N))
- α(N) = Inverse Ackermann function (almost constant)
- Nearly linear in practice

Space Complexity: O(N)
- Parent and rank arrays
"""

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Parent and rank initialization
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            # Path Compression
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0  # No merge happened

            # Union by Rank
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1  # Merge happened

        components = n

        for n1, n2 in edges:
            components -= union(n1, n2)

        return components

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (5, [[0,1],[1,2],[3,4]]),   # 2 components
        (5, [[0,1],[1,2],[2,3],[3,4]]),  # 1 component
        (4, []),  # 4 components (no edges)
    ]

    for n, edges in test_cases:
        result = sol.countComponents(n, edges)
        print(f"n={n}, edges={edges}")
        print(f"Output: {result}\n")