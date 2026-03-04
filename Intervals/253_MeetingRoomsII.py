"""
LeetCode 253: Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Problem Description:
- Given an array of meeting time intervals:
      intervals[i] = [start, end]
- Return the minimum number of conference rooms required.

Example:
intervals = [[0,30],[5,10],[15,20]] → 2
Explanation:
[0,30] overlaps with both [5,10] and [15,20],
so we need at least 2 rooms.

intervals = [[7,10],[2,4]] → 1

Approach (Two-Pointer Technique with Sorted Start & End Times):

Key Idea:
- Instead of comparing intervals directly,
  separate all start times and end times.
- If a meeting starts before another ends,
  we need a new room.
- If a meeting ends before another starts,
  we can reuse a room.

Step 1: Extract and sort start and end times
    start = sorted([i.start for i in intervals])
    end   = sorted([i.end   for i in intervals])

Step 2: Use two pointers:
    s → iterate over start times
    e → iterate over end times

Maintain:
    cur → current number of rooms being used
    res → maximum rooms needed at any time

Step 3: Iterate through all meetings:
While s < len(intervals):

    If start[s] < end[e]:
        - A meeting starts before the earliest one ends
        - Need a new room
        - cur += 1
        - s += 1

    Else:
        - A meeting ended before next one starts
        - Free a room
        - cur -= 1
        - e += 1

    Update:
        res = max(res, cur)

Return res

Why This Works:
- Sorting ensures chronological order.
- Comparing start[s] and end[e] tells us whether
  a room frees up before the next meeting starts.

Example:
intervals = [[0,30],[5,10],[15,20]]

start = [0,5,15]
end   = [10,20,30]

Process:
0 < 10 → cur=1
5 < 10 → cur=2
15 >= 10 → cur=1 (free room)
15 < 20 → cur=2

Maximum rooms needed = 2

Time Complexity: O(n log n)
- Sorting dominates.

Space Complexity: O(n)
- Two sorted lists are created.
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        res, cur = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                cur += 1
            else:
                e += 1
                cur -= 1

            res = max(res, cur)

        return res

sol = Solution()
intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
print(sol.minMeetingRooms(intervals))  # Expected: 2