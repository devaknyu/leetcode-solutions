"""
LeetCode 435: Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Problem Description:
- You are given an array of intervals where intervals[i] = [start, end].
- Return the minimum number of intervals you need to remove
  to make the rest of the intervals non-overlapping.

Examples:
intervals = [[1,2],[2,3],[3,4],[1,3]] → 1
Explanation: Remove [1,3]

intervals = [[1,2],[1,2],[1,2]] → 2

intervals = [[1,2],[2,3]] → 0

Approach (Greedy – Keep the Interval with Smaller End):

Key Idea:
- To minimize removals, we want to keep intervals that
  finish earlier.
- When two intervals overlap, we remove the one
  with the larger end time.

Step 1: Sort intervals by start time
intervals.sort(key=lambda i: i[0])

Step 2: Initialize:
- count = 0 (number of removals)
- prevEnd = intervals[0][1]

Step 3: Iterate through remaining intervals:
For each (start, end):

Case 1: No overlap
If:
    start >= prevEnd
Then:
    - Update prevEnd = end

Case 2: Overlap
Else:
    - Increment removal count
    - Keep the interval with smaller end:
          prevEnd = min(prevEnd, end)

Why keep the smaller end?
- It leaves more room for future intervals,
  reducing future overlaps.

Example:
intervals = [[1,2],[1,3],[2,4]]

After sorting:
[[1,2],[1,3],[2,4]]

Start:
prevEnd = 2

Check [1,3]:
1 < 2 → overlap
Remove one (count = 1)
Keep smaller end → prevEnd = min(2,3) = 2

Check [2,4]:
2 >= 2 → no overlap
prevEnd = 4

Answer = 1

Time Complexity: O(n log n)
- Sorting dominates.

Space Complexity: O(1)
- Only a few variables used.
"""

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
