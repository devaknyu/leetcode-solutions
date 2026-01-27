"""
LeetCode 90: Subsets II
https://leetcode.com/problems/subsets-ii/

Problem Description:
- Given an integer array nums that may contain duplicates,
  return all possible subsets (the power set).
- The solution set must not contain duplicate subsets.
- The subsets can be returned in any order.

Key Difference from LeetCode 78 (Subsets):
- nums may contain duplicate values.
- Duplicate subsets must be avoided.

Approach:
- Use Depth-First Search (DFS) with backtracking.
- Sort the input array so duplicate elements are adjacent.
- At each index, decide whether to:
  1. Include the current element.
  2. Exclude the current element and skip all of its duplicates.

Key Observations:
- Sorting allows easy detection of duplicates.
- When excluding a value, all consecutive duplicates must be skipped
  to prevent generating identical subsets.
- Each index represents a binary decision: include or exclude.
- Backtracking ensures exploration of all valid subsets.

Technique: Backtracking (DFS)
1. Start DFS from index 0 with an empty subset.
2. If index reaches the length of nums, record the subset.
3. Recursively explore:
   - Including nums[i]
   - Excluding nums[i] and skipping duplicates

Example:
nums = [1, 2, 2]

Subsets:
- [], [1]
- [2], [1, 2]
- [2, 2], [1, 2, 2]

Time Complexity:
- O(2ⁿ), where n is the number of elements
- Duplicate skipping reduces redundant paths

Space Complexity:
- O(n) for recursion depth
- O(number of unique subsets) for result storage
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset):
            # Reached the end → record subset
            if i == len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)

            # Backtrack
            subset.pop()

            # Skip all duplicates of nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i] and move forward
            dfs(i + 1, subset)

        dfs(0, [])
        return res

if __name__ == "__main__":
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))