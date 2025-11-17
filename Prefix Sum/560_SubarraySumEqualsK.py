from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0: 1}  # Base case: sum 0 appears once

        for n in nums:
            curSum += n
            diff = curSum - k  # We've seen this prefix sum before
            
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            
        return res