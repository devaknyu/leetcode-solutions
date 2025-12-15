"""
LeetCode 367: Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/

Approach:
- Check if a number is a perfect square (integer square root exists)
- Use binary search to find square root
- Return True if exact square found, False otherwise

Technique: Binary Search on Square Values
1. Search space: 0 to num
2. For each mid, compare mid² with num
3. If mid² > num, search left
4. If mid² < num, search right
5. If mid² == num, return True
6. If loop ends, return False

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
            
        l, r = 0, num
        
        while l <= r:
            m = (r + l) // 2
            square = m * m
            
            if square == num:
                return True
            elif square > num:
                r = m - 1
            else:
                l = m + 1
        
        return False
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        16,    # → True (4²)
        14,    # → False
        1,     # → True (1²)
        9,     # → True (3²)
        25,    # → True (5²)
        26,    # → False
        100,   # → True (10²)
    ]
    
    for num in test_cases:
        print(f"num = {num}")
        result = sol.isPerfectSquare(num)
        print(f"Perfect square: {result}\n")