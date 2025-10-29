import collections
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        max_length = 0

        for num in count:
            if num + 1 in count:
                length = count[num] + count[num + 1]
                if length > max_length:
                    max_length = length
        return max_length
