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