from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the object with integer k and the stream of integers nums.
        """
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        # Ensure heap size is at most k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        Adds a new integer to the stream and returns the kth largest element.
        """
        heapq.heappush(self.minHeap, val)

        # Maintain heap size
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The root is the kth largest element
        return self.minHeap[0]
