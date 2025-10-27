class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        result = 0

        for i in range(0, len(sorted_nums), 2):
            result += sorted_nums[i]
        return result