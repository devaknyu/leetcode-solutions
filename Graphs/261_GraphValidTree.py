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