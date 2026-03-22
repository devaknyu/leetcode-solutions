class Solution:
    def rotate(self, matrix):
        """
        Rotates the matrix 90 degrees clockwise in-place.
        """

        l, r = 0, len(matrix) - 1

        while l < r:

            for i in range(r - l):

                top, bottom = l, r

                # Save top-left
                topLeft = matrix[top][l + i]

                # Move bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top-left → top-right
                matrix[top + i][r] = topLeft

            # Move inward
            l += 1
            r -= 1