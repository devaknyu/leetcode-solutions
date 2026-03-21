"""
LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Approach:
- We are given an array `prices` where prices[i] is the stock price on day i.
- We can:
    → Buy a stock
    → Sell a stock
    → Cooldown (do nothing)
- Constraint:
    After selling a stock, we must wait **1 day (cooldown)** before buying again.

Goal:
- Maximize profit.

Key Observations:
- At any index `i`, we have two states:
    1. Buying state → we are allowed to buy
    2. Selling state → we are holding stock and can sell

- This naturally forms a **decision tree** → use DFS + memoization.

State Definition:
    dfs(i, buying)
    where:
        i = current day
        buying = True → we can buy
        buying = False → we must sell or hold

Transitions:

1. If buying:
    - Buy stock:
        profit = dfs(i+1, False) - prices[i]
    - Skip (cooldown):
        profit = dfs(i+1, True)

2. If selling:
    - Sell stock:
        profit = dfs(i+2, True) + prices[i]
        (i+2 because of cooldown)
    - Skip (hold stock):
        profit = dfs(i+1, False)

Take the maximum in both cases.

Technique: Dynamic Programming (Top-Down / Memoization)

Algorithm:
1. Use recursion to explore all choices
2. Memoize results using a dictionary `dp[(i, buying)]`
3. Base case: if i >= len(prices), return 0
4. Compute and store results to avoid recomputation
5. Return dfs(0, True)

Example:

prices = [1,2,3,0,2]

Optimal:
Buy at 1 → Sell at 3 → Cooldown → Buy at 0 → Sell at 2

Profit = 2 + 2 = 4

Time Complexity:
- Each state (i, buying) is computed once
- Total states: O(n * 2)
- Time Complexity: O(n)

Space Complexity:
- O(n) for recursion + memoization
"""

class Solution:
    def maxProfit(self, prices):
        """
        Returns the maximum profit with cooldown constraint.
        """

        dp = {}

        def dfs(i, buying):

            # Base case
            if i >= len(prices):
                return 0

            # Memoization check
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                # Option 1: Buy
                buy = dfs(i + 1, False) - prices[i]

                # Option 2: Skip
                cooldown = dfs(i + 1, True)

                dp[(i, buying)] = max(buy, cooldown)

            else:
                # Option 1: Sell (cooldown next day)
                sell = dfs(i + 2, True) + prices[i]

                # Option 2: Skip (hold)
                cooldown = dfs(i + 1, False)

                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,2,3,0,2], 3),
        ([1], 0),
        ([2,1,4], 3),
        ([6,1,3,2,4,7], 6),
    ]

    for prices, expected in test_cases:
        result = solution.maxProfit(prices)
        status = "✓" if result == expected else "✗"
        print(f"prices = {prices} → profit = {result} (Expected: {expected}) {status}")