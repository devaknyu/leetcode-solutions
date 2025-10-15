class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))  # Expected output: [0, 1, 1]
    print(sol.countBits(5))  # Expected output: [0, 1, 1, 2, 1, 2]
