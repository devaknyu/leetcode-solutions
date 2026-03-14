class Solution:
    def countBits(self, n: int):
        """
        Returns an array where index i contains
        the number of set bits in integer i.
        """

        dp = [0] * (n + 1)

        # Tracks the most recent power of two
        offset = 1

        for i in range(1, n + 1):

            # When we hit the next power of two
            if offset * 2 == i:
                offset = i

            # Use the DP relation
            dp[i] = 1 + dp[i - offset]

        return dp

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (0, [0]),
    ]

    for n, expected in test_cases:
        result = solution.countBits(n)
        status = "✓" if result == expected else "✗"
        print(f"n = {n} → {result} (Expected: {expected}) {status}")