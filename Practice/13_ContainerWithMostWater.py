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
