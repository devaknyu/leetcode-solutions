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