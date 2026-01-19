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
