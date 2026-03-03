"""
LeetCode 252: Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Problem Description:
- Given an array of meeting time intervals where
      intervals[i] = [start, end]
- Determine if a person can attend all meetings.
- Return True if no meetings overlap, otherwise False.

Example:
intervals = [[0,30],[5,10],[15,20]] → False
Explanation: [0,30] overlaps with [5,10]

intervals = [[7,10],[2,4]] → True

Approach (Sort + Check Adjacent Overlaps):

Key Idea:
- If two meetings overlap, the person cannot attend both.
- After sorting by start time, any overlap will appear
  between adjacent intervals.

Step 1: Sort intervals by start time:
      intervals.sort(key=lambda i: i.start)

Step 2: Compare consecutive intervals:
For each i from 1 to len(intervals)-1:
    prev = intervals[i-1]
    cur  = intervals[i]

    If:
        prev.end > cur.start
    Then:
        Overlap exists → return False

If no overlaps found → return True

Why This Works:
- Sorting ensures meetings are ordered chronologically.
- We only need to check neighboring intervals for conflicts.

Example:
intervals = [[0,30],[5,10],[15,20]]

After sorting:
[[0,30],[5,10],[15,20]]

Compare:
30 > 5 → overlap → return False

Time Complexity: O(n log n)
- Sorting dominates.

Space Complexity: O(1)
- No extra data structures used.
"""

from typing import List
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            cur = intervals[i]

            if prev.end > cur.start:
                return False

        return True

sol = Solution()
print(sol.canAttendMeetings([Interval(0,30), Interval(5,10), Interval(15,20)]))
Expected: False