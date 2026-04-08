"""
LeetCode 11: Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Approach:
- Find two lines that form container holding maximum water
- Area = width * min(height[left], height[right])
- Use two pointers starting from both ends

Technique: Two Pointers with Greedy Choice
1. Start with maximum width (pointers at both ends)
2. Calculate area and update maximum
3. Move pointer with smaller height inward
4. Continue until pointers meet

Why move smaller pointer:
- The area is limited by the smaller height
- Moving the smaller pointer might find a taller line
- Moving the larger pointer cannot increase the area

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only constant extra space
"""

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

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],  # → 49
        [1, 1],                         # → 1
        [4, 3, 2, 1, 4],               # → 16
        [1, 2, 1],                     # → 2
    ]
    
    for height in test_cases:
        print(f"Input:  {height}")
        result = sol.maxArea(height)
        print(f"Output: {result}\n")
