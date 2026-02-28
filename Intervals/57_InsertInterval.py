"""
LeetCode 57: Insert Interval
https://leetcode.com/problems/insert-interval/

Problem Description:
- You are given a list of non-overlapping intervals sorted
  in ascending order by start time.
- You are also given a new interval `newInterval`.
- Insert `newInterval` into the list such that:
    1) The list remains sorted.
    2) Overlapping intervals are merged.
- Return the updated list of intervals.

Examples:
intervals = [[1,3],[6,9]], newInterval = [2,5]
→ [[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
→ [[1,2],[3,10],[12,16]]

Approach (Single Pass – Merge While Iterating):

We iterate through each interval and compare it with newInterval.

There are 3 cases:

1) New interval comes BEFORE current interval (no overlap):
   If:
        newInterval[1] < intervals[i][0]
   Then:
        - Append newInterval to result.
        - Since intervals are sorted, we can immediately
          return result + remaining intervals.

2) Current interval comes BEFORE new interval (no overlap):
   If:
        intervals[i][1] < newInterval[0]
   Then:
        - Append current interval to result.
        - Continue checking.

3) Overlapping intervals:
   Otherwise:
        - Merge the two intervals.
        - Update newInterval as:
              [min(start), max(end)]
        - Continue checking with updated newInterval.

After the loop:
- Append the (possibly merged) newInterval.

Why this works:
- Since intervals are sorted and non-overlapping,
  once we insert newInterval before a larger interval,
  no further merges are needed.

Time Complexity: O(n)
- We traverse the list once.

Space Complexity: O(n)
- We build a new result list.
"""

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # Case 1: new interval is completely before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: current interval is completely before new interval
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # Case 3: overlapping intervals → merge
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        # If newInterval goes at the end
        res.append(newInterval)
        return res
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))  
    # Expected: [[1,5],[6,9]]

    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  
    # Expected: [[1,2],[3,10],[12,16]]
