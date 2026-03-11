"""
LeetCode 763: Partition Labels
https://leetcode.com/problems/partition-labels/

Problem Description:
- You are given a string `s`.
- Partition the string into as many parts as possible such that
  each letter appears in **at most one part**.
- Return a list containing the **size of each partition**.

Examples:
s = "ababcbacadefegdehijhklij"
→ [9,7,8]

Explanation:
Partitions:
"ababcbaca"  → size 9
"defegde"    → size 7
"hijhklij"   → size 8

Each character appears in only one partition.

s = "eccbbbbdec"
→ [10]

Explanation:
All characters overlap with each other, so the entire
string must be one partition.

Approach (Greedy):

Key Idea:
- For every character, determine the **last position**
  where it appears in the string.
- While scanning the string, we extend the partition
  until we reach the **furthest last occurrence** of any
  character inside the current partition.

Step-by-step logic:

1) First pass:
   Record the last index of every character.

   Example:
   s = "ababcbaca"

   lastIndex:
   a → 8
   b → 5
   c → 7

2) Iterate through the string while maintaining:
   size → current partition length
   end  → furthest index this partition must reach

3) For each character `c` at index `i`:
      end = max(end, lastIndex[c])

4) Increase the current partition size:
      size += 1

5) If we reach the partition boundary:
      i == end

   then we close the partition:
      append size to result
      reset size = 0

6) Continue scanning until the string ends.

Example:
s = "ababcbacadefegdehijhklij"

Step-by-step:

First partition:
a last = 8
b last = 5
c last = 7

The furthest required index becomes 8.

Indices 0 → 8
Partition size = 9

Second partition:
"defegde"

d last = 14
e last = 15
f last = 11
g last = 13

Partition ends at index 15
Size = 7

Third partition:
"hijhklij"
Size = 8

Final result:
[9,7,8]

Time Complexity: O(n)
- One pass to compute last positions
- One pass to form partitions.

Space Complexity: O(1)
- At most 26 characters stored in the dictionary.
"""

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))  # Expected: [9,7,8]
    print(sol.partitionLabels("eccbbbbdec"))                 # Expected: [10]