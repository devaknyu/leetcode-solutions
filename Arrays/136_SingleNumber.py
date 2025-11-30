"""
LeetCode 136: Single Number
https://leetcode.com/problems/single-number/

Approach:
- Find the number that appears exactly once in array where all others appear twice
- Use XOR bitwise operation to cancel out duplicate numbers

Technique: Bit Manipulation with XOR
1. XOR of a number with itself is 0: a ^ a = 0
2. XOR of a number with 0 is the number itself: a ^ 0 = a
3. XOR is commutative and associative: order doesn't matter
4. All duplicate numbers cancel each other out, leaving the single number

Why XOR works:
- Duplicate numbers XOR to 0: a ^ a = 0
- Single number XOR with 0 gives the number: 0 ^ b = b
- Example: [4,1,2,1,2] → 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1^1) ^ (2^2) = 4 ^ 0 ^ 0 = 4

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only constant extra space
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [2, 2, 1],           # → 1
        [4, 1, 2, 1, 2],     # → 4
        [1],                  # → 1
        [7, 3, 5, 3, 7],     # → 5
        [-1, -1, -2],        # → -2
    ]
    
    for nums in test_cases:
        print(f"Input:  {nums}")
        result = sol.singleNumber(nums)
        print(f"Output: {result}")
        print(f"Verification: {nums.count(result)} occurrence(s)\n")