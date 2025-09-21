"""
LeetCode 88: Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Problem:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums2 into nums1 as one sorted array. The final array should be sorted in non-decreasing order.

Note:
- nums1 has a length of m + n, with the first m elements initialized, and the rest set to 0.
- The merge should be done in-place without returning a new array.

Approach:
- Use three pointers:
    - m_idx → last valid element in nums1
    - n_idx → last element in nums2
    - right → last index in nums1
- Compare elements from the back and place the larger one at `right`.
- Continue until nums2 is exhausted (if nums1 is exhausted, just copy remaining nums2).

Time Complexity: O(m + n)   (single pass through both arrays)
Space Complexity: O(1)      (in-place)
"""


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m_idx = m - 1
        n_idx = n - 1
        right = m + n - 1

        while n_idx >= 0:
            if m_idx >= 0 and nums1[m_idx] > nums2[n_idx]:
                nums1[right] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[right] = nums2[n_idx]
                n_idx -= 1
            right -= 1

        return nums1  # for local testing (LeetCode ignores return)

# Example run for local testing
if __name__ == "__main__":
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]
    print(Solution().merge(arr1, 3, arr2, 3))  # Output: [1,2,2,3,5,6]