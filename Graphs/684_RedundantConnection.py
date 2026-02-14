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