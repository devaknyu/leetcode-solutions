class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])

        count = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # No overlap
            if start >= prevEnd:
                prevEnd = end
            # Overlap → remove one interval
            else:
                count += 1
                prevEnd = min(prevEnd, end)

        return count