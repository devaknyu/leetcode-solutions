"""
LeetCode 215: Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem Description:
- Given an integer array nums and an integer k,
  return the kth largest element in the array.
- The array does not need to be fully sorted.

Approach:
- Use the Quickselect algorithm, which is based on Quicksort.
- Instead of sorting the entire array, Quickselect
  only processes the portion of the array that contains
  the kth largest element.
- Convert the problem into finding the (n - k)th smallest element.

Key Observations:
- Full sorting would take O(n log n), which is unnecessary.
- Quickselect has an average time complexity of O(n).
- The pivot partitions the array such that:
  - Elements ≤ pivot are on the left
  - Elements > pivot are on the right
- Recursion continues only on the side containing the target index.

Technique: Quickselect (Partition-Based Selection)
1. Convert kth largest into index (n - k).
2. Choose a pivot (rightmost element).
3. Partition the array around the pivot.
4. Compare pivot index with target index:
   - If equal, return pivot.
   - If larger, recurse left.
   - If smaller, recurse right.

Time Complexity:
- Average Case: O(n)
- Worst Case: O(n²) (rare, occurs with poor pivot choices)

Space Complexity:
- O(1) extra space (in-place)
- O(n) recursion stack in worst case
"""


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to index of kth smallest
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            # Partition the array
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Place pivot in correct position
            nums[p], nums[r] = nums[r], nums[p]

            # Recurse based on pivot position
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)

if __name__ == "__main__":
    # Example 1
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))  # Expected: 5

    # Example 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))  # Expected: 4
