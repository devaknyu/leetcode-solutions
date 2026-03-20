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

