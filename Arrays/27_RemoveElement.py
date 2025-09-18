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