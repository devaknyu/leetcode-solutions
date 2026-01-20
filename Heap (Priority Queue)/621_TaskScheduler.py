from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Max heap of task frequencies
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # stores (remaining_count, available_time)

        while maxHeap or q:
            time += 1

            # Execute a task if available
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            # Re-add task from cooldown if ready
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

if __name__ == "__main__":
    # Example 1
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(Solution().leastInterval(tasks, n))  # Expected: 8

    # Example 2
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    print(Solution().leastInterval(tasks, n))  # Expected: 6

    # Example 3
    tasks = ["A", "A", "A", "A", "B", "B", "C", "C"]
    n = 2
    print(Solution().leastInterval(tasks, n))  # Expected: 10
