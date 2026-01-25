"""
LeetCode 40: Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Problem Description:
- Given a collection of candidate numbers (candidates) and a target number (target),
  return all unique combinations where the chosen numbers sum to target.
- Each number in candidates may only be used once in the combination.
- The solution set must not contain duplicate combinations.
- The combinations can be returned in any order.

Key Difference from LeetCode 39:
- Candidates may contain duplicates.
- Each candidate can be used at most once.
- We must explicitly handle duplicate values to avoid repeated combinations.

Approach:
- Use Depth-First Search (DFS) with backtracking.
- Sort the candidates array to group duplicates together.
- At each index, decide whether to:
  1. Include the current candidate and move to the next index.
  2. Skip the current candidate and all of its duplicates.

Key Observations:
- Sorting enables easy detection of duplicates.
- When skipping a number, skip *all identical consecutive values*.
- Unlike LC39, once we choose a candidate, we must move to i + 1
  (no reuse allowed).
- Backtracking ensures exploration of all valid combinations.

Technique: Backtracking (DFS)
1. Start DFS from index 0 with total sum 0.
2. If total equals target, record a copy of the current combination.
3. If total exceeds target or index is out of bounds, stop.
4. Recursively explore:
   - Including candidates[i] (move to i + 1)
   - Excluding candidates[i] and skipping duplicates

Time Complexity:
- O(2ⁿ) in the worst case, where n is the number of candidates
- Pruning via sorting and duplicate skipping improves performance

Space Complexity:
- O(n) for recursion depth
- O(number of valid combinations) for result storage
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            # Found a valid combination
            if total == target:
                res.append(cur.copy())
                return

            # Exceeded bounds or sum
            if i >= len(candidates) or total > target:
                return

            # Include current candidate (can only be used once)
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # Backtrack
            cur.pop()

            # Skip all duplicate values
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Exclude current candidate and move forward
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))