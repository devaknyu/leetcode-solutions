class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        sorted_nums = sorted(unique_nums, reverse=True)

        if len(sorted_nums) > 2:
            return sorted_nums[2]
        else:
            return sorted_nums[0]
