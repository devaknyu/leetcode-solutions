"""
LeetCode 153: Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Approach:
- Find minimum element in rotated sorted array (no duplicates)
- Use modified binary search to locate pivot point (minimum)
- Compare middle element with left/right boundaries

Technique: Modified Binary Search
1. If left <= right, array segment is sorted, min is left element
2. Compare middle with left boundary:
   - If middle >= left: min is in right half
   - Else: min is in left half (including middle)
3. Track minimum encountered during search

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]  # Initialize with first element

        while l <= r:
            # If current segment is sorted, min is nums[l]
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = (r + l) // 2
            res = min(res, nums[m])
            
            # Determine which half contains min
            if nums[m] >= nums[l]:
                # Min is in right half
                l = m + 1
            else:
                # Min is in left half (including m)
                r = m - 1
                
        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [3, 4, 5, 1, 2],     # → 1
        [4, 5, 6, 7, 0, 1, 2],  # → 0
        [11, 13, 15, 17],    # → 11 (not rotated)
        [1],                 # → 1
        [2, 1],              # → 1
    ]
    
    for nums in test_cases:
        print(f"Array: {nums}")
        result = sol.findMin(nums)
        print(f"Minimum: {result}\n")