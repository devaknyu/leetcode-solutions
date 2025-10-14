"""
LeetCode 121: Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
- You are given an array `prices`, where `prices[i]` represents the price of a stock on the i-th day.
- The goal is to find the maximum profit you can achieve by buying on one day and selling on another later day.
- Use a **two-pointer (sliding window)** approach:
  - `L` represents the **buy day**, and `R` represents the **sell day**.
  - Initially, `L = 0` (first day) and `R = 1` (next day).
- Move `R` through the array:
  - If `prices[L] < prices[R]`, calculate profit = `prices[R] - prices[L]` and update `profit` if it’s higher.
  - If `prices[L] >= prices[R]`, move `L` to `R` (a new potential buy day since it’s cheaper).
- Continue until the end of the list and return the maximum profit found.

Example:
prices = [7,1,5,3,6,4] → Buy at 1, Sell at 6 → Profit = 5  
prices = [7,6,4,3,1] → No profit possible → Profit = 0  

Time Complexity: O(n)
Space Complexity: O(1)
"""

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
    
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))  # Expected output: 5
    print(sol.maxProfit([7,6,4,3,1]))    # Expected output: 0