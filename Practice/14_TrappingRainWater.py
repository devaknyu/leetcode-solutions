"""
LeetCode 42: Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Approach:
- Calculate how much water can be trapped between elevation bars
- Use two pointers moving from both ends towards center
- Track maximum heights from left and right separately

Technique: Two Pointers with Dynamic Max Tracking
1. Use left and right pointers starting from both ends
2. Track maximum height encountered from left (maxleft) and right (maxright)
3. Water trapped at current position = min(maxleft, maxright) - current height
4. Move pointer from side with smaller maximum height

Why this works:
- The water level at any point is determined by the minimum of the maximum heights on both sides
- By moving the pointer with smaller max, we ensure we're always calculating correctly
- This approach avoids the need for extra arrays

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only constant extra space
"""

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
            
        l, r = 0, len(height) - 1
        res = 0
        maxleft, maxright = height[l], height[r]

        while l < r:
            if maxleft < maxright:
                l += 1
                maxleft = max(maxleft, height[l])
                res += maxleft - height[l]
            else:
                r -= 1
                maxright = max(maxright, height[r])
                res += maxright - height[r]
        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],  # → 6
        [4, 2, 0, 3, 2, 5],                     # → 9
        [1, 0, 1],                              # → 1
        [1],                                     # → 0
        [],                                      # → 0
    ]
    
    for height in test_cases:
        print(f"Input:  {height}")
        result = sol.trap(height)
        print(f"Output: {result}\n")