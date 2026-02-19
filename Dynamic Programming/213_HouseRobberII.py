"""
LeetCode 213: House Robber II
https://leetcode.com/problems/house-robber-ii/

Problem Description:
- You are given an integer array `nums` where `nums[i]` represents the amount of money in the i-th house.
- Unlike LeetCode 198, the houses are arranged in a CIRCLE.
- This means the first and last houses are adjacent.
- You cannot rob two adjacent houses.
- Return the maximum amount of money you can rob without alerting the police.

Key Difference from LeetCode 198:
- Since houses are circular:
    - If you rob the first house, you CANNOT rob the last.
    - If you rob the last house, you CANNOT rob the first.
- Therefore, we must break the circular condition.

Approach (Reduce to Two Linear House Robber Problems):

Observation:
We cannot take both nums[0] and nums[-1].
So we split into two cases:

1) Rob houses from index 1 → n-1  (exclude first house)
2) Rob houses from index 0 → n-2  (exclude last house)

We compute the maximum for both cases using the same logic as
LeetCode 198 (House Robber I), then return the maximum of the two.

Edge Case:
- If there is only one house, return nums[0].

Helper Function (Linear Robber Logic):
- Same optimized DP approach:
    rob1 = max up to house i-2
    rob2 = max up to house i-1

    For each value:
        new_max = max(rob2, rob1 + current)
        rob1 = rob2
        rob2 = new_max

Example:
nums = [2, 3, 2]

Case 1: helper([3, 2]) → 3
Case 2: helper([2, 3]) → 3

Final answer = max(3, 3) = 3

Example 2:
nums = [1, 2, 3, 1]

Case 1: helper([2, 3, 1]) → 3
Case 2: helper([1, 2, 3]) → 4

Final answer = max(3, 4) = 4

Time Complexity: O(n)
- We run the linear rob algorithm twice.

Space Complexity: O(1)
- Only two variables used in each helper call.
"""


from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(num):
            rob1, rob2 = 0, 0
            for i in num:
                tmp = max(rob1 + i, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2

        return max(
            helper(nums[1:]),   # Exclude first house
            helper(nums[:-1])   # Exclude last house
        )

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 3, 2]))      # Expected output: 3
    print(sol.rob([1, 2, 3, 1]))   # Expected output: 4
    print(sol.rob([1]))            # Expected output: 1