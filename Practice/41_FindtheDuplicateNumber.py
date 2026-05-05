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

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 4, 6, 3, 2, 5, 6], 6),
    ]

    for nums, expected in test_cases:
        result = solution.findDuplicate(nums)
        status = "✓" if result == expected else "✗"
        print(f"nums = {nums} → duplicate = {result} (Expected: {expected}) {status}")