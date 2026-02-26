from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LEN = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LEN[i] = max(LEN[i], LEN[j] + 1)

        return max(LEN)