"""
LeetCode 69: Sqrt(x)
https://leetcode.com/problems/sqrtx/

Approach:
- Find integer square root of x (floor value)
- Use binary search to find largest integer whose square <= x
- Return the integer part only (no decimals)

Technique: Binary Search on Square Values
1. Search space: 0 to x
2. For each mid, compare mid² with x
3. If mid² > x, search left
4. If mid² < x, update result and search right
5. If mid² == x, return mid

Time Complexity: O(log x)
Space Complexity: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = m
            else:
                return m
                
        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        4,    # → 2
        8,    # → 2 (sqrt(8) ≈ 2.828, floor is 2)
        0,    # → 0
        1,    # → 1
        16,   # → 4
        25,   # → 5
        26,   # → 5
    ]
    
    for x in test_cases:
        print(f"x = {x}")
        result = sol.mySqrt(x)
        print(f"sqrt(x) = {result} ({result}² = {result*result}, {(result+1)}² = {(result+1)*(result+1)})\n")