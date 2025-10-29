"""
LeetCode 594: Longest Harmonious Subsequence
https://leetcode.com/problems/longest-harmonious-subsequence/

Approach:
- A harmonious subsequence is defined as one where the difference between the 
  maximum and minimum elements is exactly 1.
- We can use a frequency map (Counter) to count occurrences of each number.
- For each number `num`, if `num + 1` exists in the map, we can form a valid 
  harmonious subsequence combining all occurrences of `num` and `num + 1`.
- The length of such a subsequence is `count[num] + count[num + 1]`.
- Track the maximum length found across all valid pairs.

Steps:
1. Count the frequency of all numbers using `collections.Counter`.
2. Iterate over each unique number in the counter.
3. If `num + 1` exists, compute the subsequence length and update the maximum.
4. Return the maximum length.

Example:
Input:
  nums = [1,3,2,2,5,2,3,7]
Output:
  5
Explanation:
  The longest harmonious subsequence is [3,2,2,2,3].

Time Complexity: O(n)
Space Complexity: O(n)
"""

import collections
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        max_length = 0

        for num in count:
            if num + 1 in count:
                length = count[num] + count[num + 1]
                if length > max_length:
                    max_length = length
        return max_length

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # Expected output: 5
    print(sol.findLHS([1, 1, 1, 1]))              # Expected output: 0
    print(sol.findLHS([1, 2, 3, 4]))              # Expected output: 2