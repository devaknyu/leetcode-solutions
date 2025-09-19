"""
LeetCode 35: Search Insert Position
https://leetcode.com/problems/search-insert-position/

Problem:
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Approach:
- Use a binary search (recursive in this case).
- If target is found, return its index.
- If not found, return the position where it should be inserted.
- Base case: if start > end, return start (insertion position).

Time Complexity: O(log n)   (binary search)
Space Complexity: O(log n)  (recursive stack depth, O(1) if iterative)
"""


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bin_search(start: int, end: int) -> int:
            if start > end:
                return start
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bin_search(mid + 1, end)
            else:
                return bin_search(start, mid - 1)
        
        return bin_search(0, len(nums) - 1)
