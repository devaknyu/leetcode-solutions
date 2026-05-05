from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Returns the duplicated number in the array.
        """

        # ---------- Phase 1: Detect cycle ----------
        slow = fast = 0
        while True:
            slow = nums[slow]           # Move slow by 1 step
            fast = nums[nums[fast]]     # Move fast by 2 steps
            if slow == fast:
                break

        # ---------- Phase 2: Find cycle entrance ----------
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow