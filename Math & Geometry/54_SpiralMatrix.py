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