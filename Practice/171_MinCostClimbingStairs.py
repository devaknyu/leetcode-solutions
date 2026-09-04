"""
LeetCode 746: Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

Problem Description:
- You are given an integer array `cost` where `cost[i]` is the cost of stepping on the i-th stair.
- Once you pay the cost, you can climb either 1 or 2 steps.
- You can start from step 0 or step 1.
- The goal is to reach the "top" (one step beyond the last index) with minimum total cost.

Approach (Bottom-Up Dynamic Programming – In-Place Optimization):
- The key idea is to compute the minimum cost required to reach the top starting from each step.
- From any step `i`, you can go to:
    - step `i + 1`
    - step `i + 2`
- Therefore, the recurrence relation is:
  
  cost[i] = cost[i] + min(cost[i+1], cost[i+2])

- To simplify handling the "top", we append `0` to the array.
  - This represents the cost of reaching the top.
  - Now the top behaves like a normal step with cost 0.

Step-by-step:
1. Append 0 to `cost` (representing the top).
2. Traverse the array backward starting from the third-last element.
3. For each index `i`, update:
      cost[i] += min(cost[i+1], cost[i+2])
4. The final answer is:
      min(cost[0], cost[1])
   since we are allowed to start from either step 0 or step 1.

Example:
cost = [10, 15, 20]

After appending 0:
[10, 15, 20, 0]

Backward computation:
i = 1 → cost[1] = 15 + min(20, 0) = 15
i = 0 → cost[0] = 10 + min(15, 20) = 25

Return min(25, 15) = 15

Time Complexity: O(n)
- We iterate through the array once.

Space Complexity: O(1)
- No extra DP array is used (in-place modification).
"""

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([10, 15, 20]))       # Expected output: 15
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected: 6