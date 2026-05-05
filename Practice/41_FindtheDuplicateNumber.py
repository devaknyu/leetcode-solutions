"""
LeetCode 287: Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Problem Description:
- Given an array nums containing n + 1 integers where each integer is
  in the range [1, n] inclusive.
- There is exactly one duplicated number, but it may appear more than once.
- The array must not be modified, and only constant extra space is allowed.

Approach:
- Treat the array as a linked list where:
  * Each index is a node
  * nums[i] points to the next node nums[i]
- Due to the duplicate value, a cycle must exist in this "linked list".

Key Observations:
- Since there are n + 1 nodes but only n possible values,
  at least one value must repeat (Pigeonhole Principle).
- The duplicate number corresponds to the entry point of the cycle.

Technique: Floyd’s Tortoise and Hare (Cycle Detection)
1. Use two pointers moving at different speeds to detect a cycle
2. Once a cycle is found, reset one pointer to the start
3. Move both pointers one step at a time
4. The meeting point is the duplicate number

Time Complexity:
- O(n)

Space Complexity:
- O(1), constant extra space
"""

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