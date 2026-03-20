class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Returns the number of unique paths
        from top-left to bottom-right.
        """

        # Initialize bottom row
        row = [1] * n

        # Build from bottom to top
        for i in range(m - 1):

            newRow = [1] * n

            # Traverse from right to left
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]

            row = newRow

        return row[0]

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (3, 7, 28),
        (3, 3, 6),
        (1, 5, 1),
        (5, 1, 1),
    ]

    for m, n, expected in test_cases:
        result = solution.uniquePaths(m, n)
        status = "✓" if result == expected else "✗"
        print(f"m = {m}, n = {n} → paths = {result} (Expected: {expected}) {status}")

