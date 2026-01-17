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