"""
LeetCode 198: House Robber
https://leetcode.com/problems/house-robber/

Problem Description:
- You are given an integer array `nums` where `nums[i]` represents the amount of money in the i-th house.
- You cannot rob two adjacent houses (security system constraint).
- Return the maximum amount of money you can rob without alerting the police.

Approach (Dynamic Programming – Space Optimized):

Key Idea:
- At each house, you have two choices:
    1. Rob the current house → you must skip the previous house.
    2. Skip the current house → keep the previous maximum.

Let:
- rob1 = max money up to house i-2
- rob2 = max money up to house i-1

For each house value `n`, compute:
    new_max = max(rob2, rob1 + n)

Explanation:
- rob2 → skip current house
- rob1 + n → rob current house

Then shift:
- rob1 = rob2
- rob2 = new_max

This way, we only store results for the last two states instead of a full DP array.

Example:
nums = [2, 7, 9, 3, 1]

Step-by-step:
Initial:
rob1 = 0
rob2 = 0

House 2:
new_max = max(0, 0 + 2) = 2
rob1 = 0
rob2 = 2

House 7:
new_max = max(2, 0 + 7) = 7
rob1 = 2
rob2 = 7

House 9:
new_max = max(7, 2 + 9) = 11
rob1 = 7
rob2 = 11

House 3:
new_max = max(11, 7 + 3) = 11
rob1 = 11
rob2 = 11

House 1:
new_max = max(11, 11 + 1) = 12
rob1 = 11
rob2 = 12

Final answer: 12

Time Complexity: O(n)
- We iterate through the list once.

Space Complexity: O(1)
- Only two variables are used.
"""

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            tmp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = tmp

        return rob2

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))      # Expected output: 4
    print(sol.rob([2, 7, 9, 3, 1]))   # Expected output: 12

