"""
LeetCode 56: Merge Intervals
https://leetcode.com/problems/merge-intervals/

Problem Description:
- You are given an array of intervals where intervals[i] = [start, end].
- Merge all overlapping intervals.
- Return a list of non-overlapping intervals that cover all input intervals.

Examples:
intervals = [[1,3],[2,6],[8,10],[15,18]]
→ [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
→ [[1,5]]

Approach (Sort + Greedy Merge):

Step 1: Sort the intervals
- Sort by starting time:
      intervals.sort(key=lambda i: i[0])
- This ensures overlapping intervals appear next to each other.

Step 2: Initialize result list
- Start with:
      output = [intervals[0]]
- This holds merged intervals.

Step 3: Iterate through remaining intervals
For each (start, end):

Let:
    lastEnd = output[-1][1]

Case 1: Overlapping
If:
    start <= lastEnd
Then:
    - Merge intervals.
    - Update the last interval’s end:
          output[-1][1] = max(lastEnd, end)

Case 2: No overlap
Else:
    - Append current interval to output.

Why This Works:
- Since intervals are sorted by start time,
  once an interval doesn’t overlap,
  it will not overlap with any previous intervals either.

Example:
intervals = [[1,3],[2,6],[8,10],[15,18]]

After sorting:
[[1,3],[2,6],[8,10],[15,18]]

Start with:
output = [[1,3]]

Check [2,6]:
2 <= 3 → merge → [1,6]

Check [8,10]:
8 > 6 → append

Check [15,18]:
15 > 10 → append

Final:
[[1,6],[8,10],[15,18]]

Time Complexity: O(n log n)
- Sorting dominates.

Space Complexity: O(n)
- Output list may store all intervals.
"""

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # Overlapping intervals
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)

            # Non-overlapping interval
            else:
                output.append([start, end])

        return output
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    # Expected: [[1,6],[8,10],[15,18]]

    print(sol.merge([[1,4],[4,5]]))
    # Expected: [[1,5]]