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