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
