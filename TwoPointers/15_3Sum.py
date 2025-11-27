"""
LeetCode 15: 3Sum
https://leetcode.com/problems/3sum/

Approach:
- Find all unique triplets that sum to zero
- Sort array first to enable two-pointer technique
- Skip duplicates to avoid duplicate triplets

Technique: Sorting + Two Pointers
1. Sort the array to handle duplicates and enable two-pointer
2. For each element, use two pointers to find pairs that sum to -element
3. Skip duplicate elements to avoid duplicate triplets
4. When triplet found, move pointers and skip duplicates

Time Complexity: O(n²) - sorting O(n log n) + nested loops O(n²)
Space Complexity: O(1) or O(n) depending on sort implementation
"""

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i-1] == a:
                continue 
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [-1, 0, 1, 2, -1, -4],  # → [[-1,-1,2],[-1,0,1]]
        [0, 1, 1],               # → []
        [0, 0, 0],               # → [[0,0,0]]
        [1, -1, -1, 0],          # → [[-1,0,1]]
    ]
    
    for nums in test_cases:
        print(f"Input:  {nums}")
        result = sol.threeSum(nums)
        print(f"Output: {result}\n")