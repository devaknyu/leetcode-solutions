"""
LeetCode 746: Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

Approach:
- You are given an integer array `cost` where `cost[i]` is the cost of stepping on the i-th stair.
- You can start from step 0 or step 1 and can climb either 1 or 2 steps at a time.
- The goal is to reach the "top" (beyond the last index) with the minimum total cost.

Dynamic Programming approach:
- Let `dp[i]` represent the minimum cost to reach step `i`.
- Base cases:
  - `dp[0] = 0` → No cost before the first step.
  - `dp[1] = 0` → You can start from either step 0 or 1 freely.
- Transition relation:
  - For each step `i` (starting from 2):
    `dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])`
  - This means to reach step `i`, you could have come from:
    - Step `i-1` (paying cost[i-1]), or
    - Step `i-2` (paying cost[i-2]).
  - Choose the minimum of those two options.
- Finally, `dp[n]` gives the minimum cost to reach the top (one step beyond the last stair).

Example:
cost = [10, 15, 20]
dp = [0, 0, min(0+10, 0+15)] → [0, 0, 15]
Output = 15

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([10, 15, 20]))        # Expected output: 15
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected output: 6
