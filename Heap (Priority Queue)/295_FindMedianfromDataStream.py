"""
LeetCode 295: Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Problem Description:
- Design a data structure that supports adding numbers from a data stream
  and finding the median of all elements seen so far.
- Median definition:
  - If the count is odd, median is the middle element.
  - If the count is even, median is the average of the two middle elements.

Approach:
- Use two heaps to maintain balance:
  - Max Heap (small): stores the smaller half of the numbers.
  - Min Heap (large): stores the larger half of the numbers.
- Ensure both heaps are balanced such that their sizes differ by at most one.

Key Observations:
- Python only provides a Min Heap, so the Max Heap is simulated using negation.
- The largest value in the smaller half and the smallest value in the larger
  half determine the median.
- Rebalancing ensures constant-time median retrieval.

Technique: Two Heaps (Max Heap + Min Heap)
1. Insert the new number into the max heap (small).
2. If ordering is violated, move elements between heaps.
3. Rebalance heaps so size difference is at most one.
4. Compute median based on heap sizes.

Time Complexity:
- addNum: O(log n)
- findMedian: O(1)

Space Complexity:
- O(n), to store all elements
"""


import heapq


class MedianFinder:

    def __init__(self):
        # Max heap (simulated using negatives) for smaller half
        self.small = []
        # Min heap for larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max heap
        heapq.heappush(self.small, -num)

        # Maintain ordering: max(small) <= min(large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Rebalance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Odd count
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        # Even count
        return (-self.small[0] + self.large[0]) / 2

if __name__ == "__main__":
    mf = MedianFinder()

    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # Expected: 1.5

    mf.addNum(3)
    print(mf.findMedian())  # Expected: 2.0
