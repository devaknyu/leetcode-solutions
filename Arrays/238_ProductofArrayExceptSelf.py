"""
LeetCode 238: Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Approach:
- Compute product of all elements except self without using division
- Use prefix and postfix products in separate passes
- Store prefix products in result, then multiply by postfix products

Technique: Prefix and Postfix Products
1. First pass: Calculate prefix products (products of all elements before current index)
2. Second pass: Calculate postfix products (products of all elements after current index)
3. Multiply prefix and postfix for each position to get final result

Time Complexity: O(n) - two passes through array
Space Complexity: O(1) - output array doesn't count as extra space
"""

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # Calculate prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Calculate postfix products and multiply with prefix
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [1,2,3,4],    # → [24,12,8,6]
        [-1,1,0,-3,3], # → [0,0,9,0,0]
        [2,3,5],       # → [15,10,6]
    ]
    
    for nums in test_cases:
        print(f"Input:  {nums}")
        result = sol.productExceptSelf(nums)
        print(f"Output: {result}\n")