class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                dp[i] += dp[i + 2]

        return dp[0]
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))   # Expected: 2
    print(sol.numDecodings("226"))  # Expected: 3
    print(sol.numDecodings("06"))   # Expected: 0
