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