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