from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # Build heap with (distance, x, y)
        for x, y in points:
            dist = x * x + y * y
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        res = []

        # Extract k closest points
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res

if __name__ == "__main__":
    # Example 1
    points = [[1, 3], [-2, 2]]
    k = 1
    print(Solution().kClosest(points, k))
    # Expected: [[-2, 2]]

    # Example 2
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(Solution().kClosest(points, k))
    # Expected: Two closest points to origin
