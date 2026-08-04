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

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([3, 6, 7, 11], 8),   # → 4
        ([30, 11, 23, 4, 20], 5),  # → 30
        ([30, 11, 23, 4, 20], 6),  # → 23
        ([1], 1),             # → 1
    ]
    
    for piles, h in test_cases:
        print(f"Piles: {piles}, Hours: {h}")
        result = sol.minEatingSpeed(piles, h)
        print(f"Min eating speed: {result}\n")