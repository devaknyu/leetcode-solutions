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