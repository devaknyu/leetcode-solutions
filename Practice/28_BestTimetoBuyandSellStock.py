class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        L, R = 0, 1
        profit = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                newP = prices[R] - prices[L]
                profit = max(newP, profit)
            else:
                L = R
            R += 1
        return profit