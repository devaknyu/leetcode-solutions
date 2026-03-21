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