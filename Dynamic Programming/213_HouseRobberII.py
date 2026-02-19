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