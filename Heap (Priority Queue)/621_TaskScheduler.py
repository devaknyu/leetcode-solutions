"""
LeetCode 621: Task Scheduler
https://leetcode.com/problems/task-scheduler/

Problem Description:
- You are given a list of tasks represented by capital letters.
- Each task takes exactly 1 unit of time to complete.
- The same task must be separated by at least n units of time (cooldown).
- You may perform idle operations if no task is available.
- Return the minimum number of units of time required to finish all tasks.

Approach:
- Use a Max Heap to always schedule the task with the highest remaining count.
- Use a Queue to manage tasks that are cooling down.
- Simulate the CPU execution one time unit at a time.

Key Observations:
- Executing the most frequent task first reduces idle time.
- After executing a task, it must wait n units before being reused.
- The queue tracks tasks along with the time they become available again.
- The simulation continues until all tasks are completed.

Technique: Max Heap + Queue (Greedy Simulation)
1. Count task frequencies.
2. Push counts into a max heap (using negative values).
3. Initialize a queue to store cooling tasks as (remaining_count, available_time).
4. For each time unit:
   - Execute the most frequent available task.
   - Put it into cooldown if it still has remaining executions.
   - Reinsert tasks from the queue when cooldown expires.

Time Complexity:
- O(T log T), where T is the number of tasks.
- Each task is pushed and popped from the heap once.

Space Complexity:
- O(T), for the heap and cooldown queue.
"""


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
