"""
LeetCode 2013: Detect Squares
https://leetcode.com/problems/detect-squares/

Approach:
- We design a data structure that supports:
    1. add(point) → add a point to the structure
    2. count(point) → count the number of axis-aligned squares
       that can be formed using the given point

Square Properties:
- All sides must be equal
- Must be axis-aligned → edges parallel to x and y axes
- Given one point (px, py), we need 3 other points:
    (x, y) → diagonal point
    (x, py) → horizontal partner
    (px, y) → vertical partner

Key Observations:
- A valid square requires:
    |px - x| == |py - y|  → equal side lengths
- Also:
    x != px and y != py (not same row or column)

Core Idea:
- Treat each existing point (x, y) as a potential diagonal
- If it forms a square with (px, py), then:
    → Count how many times (x, py) exists
    → Count how many times (px, y) exists
- Multiply these counts to get total combinations

Technique: HashMap + Geometry

Data Structures:
- ptsCount: dictionary mapping point → frequency
- pts: list of all added points (to iterate diagonals)

Algorithm:

add(point):
1. Increment frequency in ptsCount
2. Append point to pts list

count(point):
1. Initialize result = 0
2. For each point (x, y) in pts:
   - Check if it can form a diagonal:
       abs(px - x) == abs(py - y)
       x != px and y != py
   - If valid:
       res += count[(x, py)] * count[(px, y)]
3. Return result

Example:

Add:
(3,10), (11,2), (3,2)

Query:
count((11,10))

Possible square:
(11,10), (3,10), (11,2), (3,2)

→ result = 1

Time Complexity:
- add → O(1)
- count → O(n), where n = number of points

Space Complexity:
- O(n)
"""

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

# Example usage
if __name__ == "__main__":
    cs = CountSquares()

    cs.add([3, 10])
    cs.add([11, 2])
    cs.add([3, 2])

    print(cs.count([11, 10]))  # Expected: 1

    cs.add([11, 2])  # duplicate point
    print(cs.count([11, 10]))  # Expected: 2