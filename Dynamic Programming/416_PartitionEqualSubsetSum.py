"""
LeetCode 416: Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Problem Description:
- Given a non-empty array `nums` containing only positive integers,
  determine if the array can be partitioned into two subsets
  such that the sum of elements in both subsets is equal.

Examples:
nums = [1,5,11,5] → True
Explanation: [1,5,5] and [11]

nums = [1,2,3,5] → False

Key Insight:
- If total sum is odd → impossible.
- If total sum is even → we need to check whether
  a subset exists whose sum equals total_sum / 2.

This becomes a Subset Sum problem.

Approach (Dynamic Programming using a Set):

Step 1:
- Compute total sum.
- If sum(nums) % 2 != 0 → return False.
- Let target = sum(nums) // 2.

Step 2:
- Use a set `dp` to store all possible subset sums.
- Initialize:
      dp = {0}
  (We can always form sum 0 by choosing nothing.)

Step 3:
- Iterate through numbers (right to left).
- For each number nums[i]:
    - Create a new set `nextDp`.
    - For each existing sum j in dp:
          1) Include nums[i] → j + nums[i]
          2) Exclude nums[i] → j
    - If at any point j + nums[i] == target → return True.
    - Update dp = nextDp.

Step 4:
- If no subset equals target → return False.

Example:
nums = [1,5,11,5]
total = 22 → target = 11

Possible subset sums gradually build:
{0}
{0,5}
{0,5,11,16}
...
When 11 appears → return True

Time Complexity: O(n * target)
- In worst case, dp can grow up to size target.

Space Complexity: O(target)
- We store possible subset sums up to target.
"""


from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for j in dp:
                if target == j + nums[i]:
                    return True
                nextDp.add(j + nums[i])
                nextDp.add(j)
            dp = nextDp

        return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition([1,5,11,5]))  # Expected: True
    print(sol.canPartition([1,2,3,5]))   # Expected: False