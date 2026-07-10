import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (r + l) // 2
            hour = 0
            # Calculate total hours needed at speed m
            for p in piles:
                hour += math.ceil(p / m)
            
            if hour <= h:
                # Valid speed, try slower
                res = min(res, m)
                r = m - 1
            else:
                # Need faster speed
                l = m + 1
        return res