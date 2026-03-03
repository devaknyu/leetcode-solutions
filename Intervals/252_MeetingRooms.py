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