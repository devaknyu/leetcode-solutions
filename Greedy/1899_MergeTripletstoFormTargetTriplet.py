"""
LeetCode 1899: Merge Triplets to Form Target Triplet
https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

Problem Description:
- You are given a list of triplets `triplets`, where each triplet
  contains three integers.
- You are also given a `target` triplet.

Operation Allowed:
- You may choose two triplets and **merge** them.
- When merging triplets A and B, the resulting triplet becomes:

      [max(A[0], B[0]), max(A[1], B[1]), max(A[2], B[2])]

Goal:
- Determine whether it is possible to obtain the `target`
  triplet after performing any number of merges.

Examples:
triplets = [[2,5,3],[1,8,4],[1,7,5]]
target   = [2,7,5]
→ True

Explanation:
We can merge:
[2,5,3] and [1,7,5]

Result:
[max(2,1), max(5,7), max(3,5)]
= [2,7,5] → target achieved.

Example 2:
triplets = [[3,4,5],[4,5,6]]
target   = [3,2,5]
→ False

Explanation:
The second value in all triplets is greater than target[1],
so it is impossible to form the target.

Example 3:
triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target   = [5,5,5]
→ True

Approach (Greedy Filtering):

Key Idea:
- We only care about triplets that **do not exceed the target**.
- If a triplet has any value greater than the corresponding
  value in the target, it can never be used in a valid merge.

Goal:
- Find triplets that match each component of the target.

Specifically we want:
- one triplet with value = target[0]
- one triplet with value = target[1]
- one triplet with value = target[2]

These triplets can be merged together to form the target.

Step-by-step logic:

1) Create a set `good` to track which target positions
   we have successfully matched.

2) Iterate through every triplet `t`.

3) Skip invalid triplets:
      if t[i] > target[i] for any index → ignore it

4) For valid triplets:
   check each index `i`:
      if t[i] == target[i]
         add `i` to the set `good`

5) If we eventually match all three positions:
      len(good) == 3
   then forming the target is possible.

Example:
triplets = [[2,5,3],[1,8,4],[1,7,5]]
target   = [2,7,5]

Step-by-step:

Triplet [2,5,3]
Matches target[0] → good = {0}

Triplet [1,8,4]
Invalid because 8 > target[1] → skip

Triplet [1,7,5]
Matches target[1] and target[2]
good = {0,1,2}

Since all indices matched → True.

Time Complexity: O(n)
- Single pass through all triplets.

Space Complexity: O(1)
- The set `good` stores at most 3 indices.
"""

from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))  # Expected: True
    print(sol.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))          # Expected: False