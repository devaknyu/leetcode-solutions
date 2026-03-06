"""
LeetCode 55: Jump Game
https://leetcode.com/problems/jump-game/

Problem Description:
- You are given an integer array `nums`.
- Each element represents your maximum jump length at that position.
- Starting at index 0, determine if you can reach the last index.

Examples:
nums = [2,3,1,1,4]
→ True
Explanation: Jump 1 step to index 1, then 3 steps to the last index.

nums = [3,2,1,0,4]
→ False
Explanation: You will get stuck at index 3 because nums[3] = 0.

nums = [2,0]
→ True

Approach (Greedy - Backward Goal Tracking):

Key Idea:
- Instead of jumping forward, we work **backward from the last index**.
- We keep moving the goal position to the left whenever we find an
  index that can reach the current goal.

Step-by-step logic:

1) Initialize:
   goal → last index of the array

2) Traverse the array backwards.

3) For each index `i`, check if:
      i + nums[i] >= goal

4) If true:
      move the goal to index `i`
   because from `i` we can reach the previous goal.

5) Continue until the beginning of the array.

6) If the goal becomes index 0:
      return True
   otherwise:
      return False

Example:
nums = [2,3,1,1,4]

Initial goal = 4

Process:

i = 4 → 4 + 4 >= 4 → goal = 4
i = 3 → 3 + 1 >= 4 → goal = 3
i = 2 → 2 + 1 >= 3 → goal = 2
i = 1 → 1 + 3 >= 2 → goal = 1
i = 0 → 0 + 2 >= 1 → goal = 0

Since goal reached index 0 → return True.

Example 2:
nums = [3,2,1,0,4]

Initial goal = 4

Process:

i = 4 → 4 + 4 >= 4 → goal = 4
i = 3 → 3 + 0 < 4 → cannot reach goal
i = 2 → 2 + 1 < 4 → cannot reach goal
i = 1 → 1 + 2 < 4 → cannot reach goal
i = 0 → 0 + 3 < 4 → cannot reach goal

Goal never reaches 0 → return False.

Time Complexity: O(n)
- We iterate through the array once.

Space Complexity: O(1)
- Only one variable (`goal`) is used.
"""

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))  # Expected: True
    print(sol.canJump([3,2,1,0,4]))  # Expected: False
    print(sol.canJump([2,0]))        # Expected: True