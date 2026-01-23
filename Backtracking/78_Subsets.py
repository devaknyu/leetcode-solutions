"""
LeetCode 78: Subsets
https://leetcode.com/problems/subsets/

Problem Description:
- Given an integer array nums with unique elements,
  return all possible subsets (the power set).
- The solution must not contain duplicate subsets.
- Subsets can be returned in any order.

Approach:
- Use Depth-First Search (DFS) with backtracking.
- At each index, choose whether to include or exclude the current element.
- This generates all 2ⁿ possible subsets.

Key Observations:
- Each element has exactly two choices: include or exclude.
- Backtracking allows exploring all combinations efficiently.
- A copy of the current subset must be stored to avoid mutation issues.

Technique: Backtracking (DFS)
1. Start DFS from index 0.
2. At each index:
   - Include nums[i] and recurse.
   - Exclude nums[i] and recurse.
3. When index reaches the end, record the subset.

Time Complexity:
- O(2ⁿ), where n is the number of elements

Space Complexity:
- O(n) for recursion depth
- O(2ⁿ) for storing all subsets
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
