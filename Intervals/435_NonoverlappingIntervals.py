from typing import List
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

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # Expected: 1
    print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))        # Expected: 2
    print(sol.eraseOverlapIntervals([[1,2],[2,3]]))              # Expected: 0
