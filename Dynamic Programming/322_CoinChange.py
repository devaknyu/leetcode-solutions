"""
LeetCode 322: Coin Change
https://leetcode.com/problems/coin-change/

Problem Description:
- You are given an integer array `coins` representing coin denominations.
- You are also given an integer `amount` representing a total amount of money.
- Return the fewest number of coins needed to make up that amount.
- If it is not possible to make that amount, return -1.
- You may use each coin unlimited times.

Examples:
coins = [1, 2, 5], amount = 11  → 3
Explanation: 11 = 5 + 5 + 1

coins = [2], amount = 3 → -1
Explanation: Impossible to form 3 using only coin 2.

Approach (Bottom-Up Dynamic Programming):

Key Idea:
- Let dp[a] represent the minimum number of coins needed to make amount `a`.
- We build the solution from 0 up to `amount`.

Initialization:
- Create a DP array of size (amount + 1).
- Initialize all values to amount + 1 (a sentinel value representing impossible).
- Set dp[0] = 0 because 0 coins are needed to make amount 0.

Transition:
For each amount `a` from 1 to `amount`:
    For each coin `c`:
        If a - c >= 0:
            dp[a] = min(dp[a], 1 + dp[a - c])

Explanation:
- If we use coin `c`, then:
      total coins = 1 (current coin) + dp[a - c]
- Take the minimum across all possible coins.

Final Step:
- If dp[amount] is still amount + 1, return -1 (impossible).
- Otherwise, return dp[amount].

Example:
coins = [1, 2, 5], amount = 5

dp initially:
[0, 6, 6, 6, 6, 6]   (since amount+1 = 6)

After computation:
dp becomes:
[0, 1, 1, 2, 2, 1]

Answer = dp[5] = 1 (using coin 5)

Time Complexity: O(amount * number_of_coins)
- For each amount, we iterate through all coins.

Space Complexity: O(amount)
- We store a DP array of size amount + 1.
"""

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # Expected: 3
    print(sol.coinChange([2], 3))        # Expected: -1