from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # Calculate current area
            width = r - l
            current_height = min(height[l], height[r])
            area = width * current_height
            res = max(res, area)

            # Move pointer with smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res