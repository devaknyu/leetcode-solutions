"""
LeetCode 39: Combination Sum
https://leetcode.com/problems/combination-sum/

Problem Description:
- Given an array of distinct integers candidates and a target integer target,
  return all unique combinations where the chosen numbers sum to target.
- You may use the same number from candidates an unlimited number of times.
- The combinations can be returned in any order.

Approach:
- Use Depth-First Search (DFS) with backtracking.
- At each step, decide whether to:
  1. Include the current candidate (and stay at the same index).
  2. Skip the current candidate and move to the next index.
- Stop exploring a path if the sum exceeds the target.

Key Observations:
- Reusing elements is allowed → do NOT increment index after choosing.
- Skipping an element requires moving to the next index.
- Backtracking ensures all valid combinations are explored without duplicates.

Technique: Backtracking (DFS)
1. Start DFS from index 0 with total sum 0.
2. If total equals target, record the current combination.
3. If total exceeds target or index is out of bounds, stop.
4. Recursively explore:
   - Including candidates[i]
   - Excluding candidates[i]

Time Complexity:
- O(2ᵗ), where t is the target value (upper bound)
- Actual performance depends on pruning effectiveness

Space Complexity:
- O(t) for recursion depth
- O(number of valid combinations) for result storage
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Found a valid combination
            if total == target:
                res.append(cur.copy())
                return

            # Exceeded bounds or sum
            if i >= len(candidates) or total > target:
                return

            # Include current candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Exclude current candidate
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
