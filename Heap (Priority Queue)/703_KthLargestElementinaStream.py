"""
LeetCode 703: Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Problem Description:
- Design a class to find the kth largest element in a stream of integers.
- The class should support:
  1. Initializing with an integer k and a list of numbers.
  2. Adding new values to the stream.
- After each addition, return the kth largest element among all elements seen so far.

Approach:
- Use a Min Heap of size k to track the k largest elements.
- The smallest element in the heap will always represent the kth largest value.
- This avoids sorting the entire stream after each insertion.

Key Observations:
- Keeping all elements is unnecessary and inefficient.
- A min heap of size k ensures:
  - Heap always contains the k largest elements seen so far.
  - The root of the heap is the kth largest element.
- If heap size exceeds k, remove the smallest element.

Technique: Min Heap
1. Initialize the heap using the given list of numbers.
2. Convert the list into a heap using heapify.
3. Remove elements until heap size is exactly k.
4. For each new value:
   - Push it into the heap.
   - If heap size exceeds k, pop the smallest element.
   - Return the heap root.

Time Complexity:
- Initialization:
  - O(n) for heapify
  - O(n log k) for trimming heap to size k
- Add operation:
  - O(log k)

Space Complexity:
- O(k), since the heap stores only k elements
"""


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

# Example usage
if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))   # 4
    print(kthLargest.add(5))   # 5
    print(kthLargest.add(10))  # 5
    print(kthLargest.add(9))   # 8
    print(kthLargest.add(4))   # 8
