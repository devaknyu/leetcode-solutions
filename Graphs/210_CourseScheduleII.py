from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()   # Fully processed nodes
        cycle = set()   # Nodes in current DFS path
        result = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            visit.add(crs)
            result.append(crs)  # Postorder → prerequisite first
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (2, [[1, 0]]),                     # [0,1]
        (4, [[1,0],[2,0],[3,1],[3,2]]),    # One valid: [0,1,2,3] or [0,2,1,3]
        (2, [[1,0],[0,1]]),                # Cycle → []
    ]

    for numCourses, prereqs in test_cases:
        result = sol.findOrder(numCourses, prereqs)
        print(f"numCourses={numCourses}, prerequisites={prereqs}")
        print(f"Output: {result}\n")