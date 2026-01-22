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
