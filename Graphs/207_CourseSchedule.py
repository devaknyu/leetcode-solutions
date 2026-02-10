from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Stores courses in the current DFS path
        visiting = set()

        def dfs(crs):
            # Cycle detected
            if crs in visiting:
                return False

            # Course already verified (no prerequisites left)
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            # Memoization: mark course as completed
            preMap[crs] = []
            return True

        # Run DFS for every course
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (2, [[1, 0]], True),                # Can finish
        (2, [[1, 0], [0, 1]], False),        # Cycle
        (4, [[1,0],[2,1],[3,2]], True),      # Linear dependency
        (3, [[0,1],[1,2],[2,0]], False),     # Cycle
    ]

    for numCourses, prereqs, expected in test_cases:
        result = sol.canFinish(numCourses, prereqs)
        print(f"numCourses={numCourses}, prerequisites={prereqs}")
        print(f"Output: {result} | Expected: {expected}\n")