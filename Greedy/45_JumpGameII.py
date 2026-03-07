"""
LeetCode 45: Jump Game II
https://leetcode.com/problems/jump-game-ii/

Problem Description:
- You are given an integer array `nums`.
- Each element represents the maximum jump length from that position.
- Starting at index 0, return the **minimum number of jumps**
  needed to reach the last index.

- It is guaranteed that you can always reach the last index.

Examples:
nums = [2,3,1,1,4]
→ 2
Explanation:
Jump 1 step from index 0 → index 1
Then jump 3 steps → index 4

nums = [2,3,0,1,4]
→ 2

nums = [1,1,1,1]
→ 3

Approach (Greedy + BFS Layer Style):

Key Idea:
- Treat the array like **levels of reachable indices**.
- From a current range of indices, we determine the **farthest
  position we can reach with one more jump**.

Think of it like **Breadth-First Search layers**:
- Each layer represents all positions reachable with the current
  number of jumps.
- We compute the farthest next position from that layer.

Step-by-step logic:

1) Maintain three variables:
   l → left boundary of current range
   r → right boundary of current range
   res → number of jumps made

2) Initially:
      l = 0
      r = 0
   This means we start at index 0.

3) While we haven't reached the last index:

   - Check every position in the range [l, r].
   - Compute the farthest position reachable:
        longest = max(i + nums[i])

4) After scanning the range:
      move to the next layer
      l = r + 1
      r = longest

5) Increment the jump count:
      res += 1

6) Continue until `r` reaches or passes the last index.

Example:
nums = [2,3,1,1,4]

Initial:
l = 0, r = 0, res = 0

Layer 1:
Indices we can explore: [0]

i = 0 → 0 + nums[0] = 2
longest = 2

Update:
l = 1
r = 2
res = 1

Layer 2:
Indices we can explore: [1,2]

i = 1 → 1 + 3 = 4
i = 2 → 2 + 1 = 3
longest = 4

Update:
l = 3
r = 4
res = 2

Now r >= last index → stop.

Final answer = 2

Example 2:
nums = [1,1,1,1]

Layer exploration:

[0] → reach 1 → jumps = 1
[1] → reach 2 → jumps = 2
[2] → reach 3 → jumps = 3

Final answer = 3

Time Complexity: O(n)
- Each index is processed at most once across the layers.

Space Complexity: O(1)
- Only a few variables are used.
"""

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            longest = 0

            for i in range(l, r + 1):
                longest = max(longest, i + nums[i])

            l = r + 1
            r = longest
            res += 1

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2,3,1,1,4]))  # Expected: 2
    print(sol.jump([2,3,0,1,4]))  # Expected: 2
    print(sol.jump([1,1,1,1]))    # Expected: 3