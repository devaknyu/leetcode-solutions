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
