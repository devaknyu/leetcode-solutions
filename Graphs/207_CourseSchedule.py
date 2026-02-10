"""
LeetCode 207: Course Schedule
https://leetcode.com/problems/course-schedule/

Approach:
- Model courses as a directed graph where an edge points from a course
  to its prerequisite
- The problem reduces to checking whether the graph contains a cycle
- If a cycle exists, it is impossible to finish all courses

Technique: DFS Cycle Detection (Directed Graph)
1. Build adjacency list mapping each course to its prerequisites
2. Use DFS to traverse prerequisite chains
3. Maintain a `visiting` set to track nodes in the current DFS path
4. If a node is revisited while in `visiting`, a cycle is detected
5. After processing a course, clear its prerequisites (memoization)

Time Complexity: O(V + E)
- V = number of courses
- E = number of prerequisite pairs

Space Complexity: O(V + E)
- Adjacency list + recursion stack + visiting set
"""

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