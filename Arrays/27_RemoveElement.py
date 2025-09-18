"""
LeetCode 27: Remove Element
https://leetcode.com/problems/remove-element/

Problem:
Given an integer array nums and an integer val, remove all occurrences of val in-place. 
The relative order of the elements may be changed.

Return the number of elements in nums which are not equal to val.
The first k elements of nums should contain the elements not equal to val.

Approach:
- Use a pointer `k` to track the next valid position in nums.
- Iterate through nums:
  - If nums[i] != val, copy nums[i] to nums[k] and increment k.
- At the end, k will represent the number of valid elements.

Time Complexity: O(n)   (single pass through array)
Space Complexity: O(1)  (in-place, no extra data structure)
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
    # Example run for local testing
if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    k = Solution().removeElement(nums, val)
    print(k)            # Output: 2
    print(nums[:k])     # Output: [2, 2]