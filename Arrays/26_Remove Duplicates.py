"""
LeetCode 26: Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Problem:
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Return the number of unique elements in nums.
The first k elements of nums should contain the unique elements in order.

Approach:
- Use two pointers:
  - `i` iterates over the array.
  - `j` tracks the position of the next unique element.
- If nums[i] != nums[i-1], it means nums[i] is unique, so assign nums[j] = nums[i] and increment j.
- At the end, j will represent the count of unique elements.

Time Complexity: O(n)   (single pass through array)
Space Complexity: O(1)  (in-place, no extra data structure)
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

# Example run for local testing
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = Solution().removeDuplicates(nums)
    print(k)            # Output: 5
    print(nums[:k])     # Output: [0, 1, 2, 3, 4]
