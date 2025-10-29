from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        product = max(
            sorted_nums[0] * sorted_nums[1] * sorted_nums[2],
            sorted_nums[0] * sorted_nums[-1] * sorted_nums[-2]
        )
        return product