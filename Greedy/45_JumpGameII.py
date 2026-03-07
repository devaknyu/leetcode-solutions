from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            longest = 0

            for i in range(l, r + 1):
                longest = max(longest, i + nums[i])

            l = r + 1
            r = longest
            res += 1

        return res