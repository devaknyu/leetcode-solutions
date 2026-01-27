"""
LeetCode 46: Permutations
https://leetcode.com/problems/permutations/

Problem Description:
- Given an array nums of distinct integers,
  return all possible permutations.
- You can return the answer in any order.

Approach:
- Use recursion by fixing one element at a time.
- Generate permutations of the remaining elements.
- Insert the fixed element into every possible position
  of each smaller permutation.

Key Observations:
- A permutation of size n can be built from permutations of size n-1.
- For each permutation of nums[1:], insert nums[0] at all positions.
- This guarantees all unique permutations without duplicates
  since all elements are distinct.

Technique: Recursive Construction
1. Base case:
   - If nums is empty, return [[]] (one empty permutation).
2. Recursively compute permutations of nums[1:].
3. For each smaller permutation:
   - Insert nums[0] at every possible index (0 to len(p)).
4. Collect all generated permutations and return.

Example:
nums = [1, 2, 3]

Step 1:
- Permutations of [2, 3] → [[2, 3], [3, 2]]

Step 2:
- Insert 1 into each position:
  - [1, 2, 3], [2, 1, 3], [2, 3, 1]
  - [1, 3, 2], [3, 1, 2], [3, 2, 1]

Time Complexity:
- O(n × n!)
  - There are n! permutations
  - Each insertion takes O(n)

Space Complexity:
- O(n × n!) for storing all permutations
- O(n) recursion depth
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: one empty permutation
        if len(nums) == 0:
            return [[]]

        # Get permutations of remaining elements
        perms = self.permute(nums[1:])
        res = []

        # Insert nums[0] into every position of each permutation
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
