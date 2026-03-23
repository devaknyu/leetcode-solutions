class Solution:
    def spiralOrder(self, matrix):
        """
        Returns elements of the matrix in spiral order.
        """

        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        res = []

        while l < r and top < bottom:

            # Traverse top row
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            # Traverse right column
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1

            # Check boundaries before continuing
            if not (l < r and top < bottom):
                break

            # Traverse bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]],
         [1,2,3,6,9,8,7,4,5]),

        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]],
         [1,2,3,4,8,12,11,10,9,5,6,7]),

        ([[1]],
         [1]),
    ]

    for matrix, expected in test_cases:
        result = solution.spiralOrder(matrix)
        status = "✓" if result == expected else "✗"
        print(f"matrix = {matrix} → spiral = {result} (Expected: {expected}) {status}")