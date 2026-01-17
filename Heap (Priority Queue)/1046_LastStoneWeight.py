"""
LeetCode 1046: Last Stone Weight
https://leetcode.com/problems/last-stone-weight/

Problem Description:
- You are given an array of integers representing the weights of stones.
- Each turn:
  1. Take the two heaviest stones.
  2. Smash them together.
     - If they are equal, both are destroyed.
     - If they are different, the remaining stone has weight |x - y|.
- Repeat until at most one stone remains.
- Return the weight of the last remaining stone, or 0 if none remain.

Approach:
- Use a Max Heap to always access the two heaviest stones efficiently.
- Since Python provides a Min Heap by default, store negative values
  to simulate Max Heap behavior.
- Repeatedly remove the two largest stones and insert the difference
  (if non-zero) back into the heap.

Key Observations:
- Sorting on every turn would be inefficient.
- A heap ensures O(log n) access to the largest elements.
- If all stones are destroyed, the heap becomes empty.
- Appending 0 at the end safely handles the edge case of an empty heap.

Technique: Heap (Max Heap via Negation)
1. Convert all stone weights to negative values.
2. Heapify the list to create a Max Heap.
3. While more than one stone exists:
   - Pop the two largest stones.
   - If they differ, push the remaining weight back.
4. Return the remaining stone weight or 0.

Time Complexity:
- Heapify: O(n)
- Each smash operation: O(log n)
- Overall: O(n log n)

Space Complexity:
- O(n), for storing stones in the heap
"""


from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to negative values to simulate a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # Smash stones until one or none remain
        while len(stones) > 1:
            first = heapq.heappop(stones)   # largest stone
            second = heapq.heappop(stones)  # second largest stone

            # If they are not equal, push the remaining stone
            if second > first:
                heapq.heappush(stones, first - second)

        # Edge case: if all stones are destroyed, heap may be empty
        stones.append(0)

        return abs(stones[0])

if __name__ == "__main__":
    # Example 1
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones))  # Expected: 1

    # Example 2
    stones = [1]
    print(Solution().lastStoneWeight(stones))  # Expected: 1

    # Example 3 (All stones destroyed)
    stones = [1, 1]
    print(Solution().lastStoneWeight(stones))  # Expected: 0
