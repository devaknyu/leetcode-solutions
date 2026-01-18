"""
LeetCode 973: K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Problem Description:
- You are given an array of points where points[i] = [xi, yi].
- The distance between a point and the origin (0, 0) is:
  √(xi² + yi²).
- Return the k closest points to the origin.
- The answer can be returned in any order.

Approach:
- Use a Min Heap to efficiently retrieve the closest points.
- Instead of computing the square root, use squared distance
  (x² + y²) to preserve ordering and improve performance.
- Store each point in the heap as (distance, x, y).

Key Observations:
- Calculating exact distance is unnecessary for comparison.
- Heap allows extracting the smallest distance in O(log n).
- Only k extractions are needed.

Technique: Min Heap
1. Iterate through all points and compute squared distance.
2. Push (distance, x, y) into the heap.
3. Heapify the list.
4. Pop k elements from the heap and collect their coordinates.

Time Complexity:
- Heapify: O(n)
- Extracting k elements: O(k log n)
- Overall: O(n + k log n)

Space Complexity:
- O(n), for storing all points in the heap
"""


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
