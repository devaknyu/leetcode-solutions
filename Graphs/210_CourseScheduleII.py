"""
LeetCode 210: Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

Approach:
- Model courses as a directed graph where edges point from a course
  to its prerequisite
- We need to return a valid ordering of courses
- If a cycle exists, no valid ordering is possible
- Use DFS with cycle detection to perform Topological Sort

Technique: DFS Topological Sort with Cycle Detection
1. Build adjacency list mapping each course to its prerequisites
2. Use DFS to traverse prerequisite chains
3. Maintain:
   - `cycle` set → tracks nodes in current DFS path (detect cycles)
   - `visit` set → tracks fully processed nodes
4. If a cycle is detected, return empty list
5. Add course to result AFTER exploring prerequisites (postorder)

Time Complexity: O(V + E)
- V = number of courses
- E = number of prerequisite pairs

Space Complexity: O(V + E)
- Adjacency list + recursion stack + sets
"""

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