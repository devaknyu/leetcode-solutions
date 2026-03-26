from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point):
        """
        Adds a point to the data structure.
        """
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point):
        """
        Returns number of squares that can be formed
        with the given point.
        """

        res = 0
        px, py = point

        for x, y in self.pts:

            # Check if (x, y) can be a diagonal
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue

            # Multiply counts of the other two required points
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res