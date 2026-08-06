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