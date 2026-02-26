"""
LeetCode 300: Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Problem Description:
- Given an integer array `nums`, return the length of the
  longest strictly increasing subsequence.
- A subsequence is derived by deleting some or no elements
  without changing the order of the remaining elements.

Examples:
nums = [10,9,2,5,3,7,101,18] → 4
Explanation: The LIS is [2,3,7,101]

nums = [0,1,0,3,2,3] → 4
nums = [7,7,7,7,7] → 1

Approach (Bottom-Up Dynamic Programming – O(n^2)):

Key Idea:
- Let LEN[i] represent the length of the longest increasing
  subsequence starting at index i.
- Every element by itself forms a subsequence of length 1.

Initialization:
LEN = [1] * len(nums)

Transition:
- Traverse from right to left.
- For each index i:
    Check all indices j > i
    If nums[i] < nums[j]:
        LEN[i] = max(LEN[i], 1 + LEN[j])

Explanation:
- If nums[i] < nums[j], we can extend the increasing subsequence
  starting at j by including nums[i].
- So we update:
      LEN[i] = max(LEN[i], LEN[j] + 1)

Final Answer:
- The result is max(LEN)
  (The LIS could start at any index.)

Example:
nums = [10,9,2,5,3,7,101,18]

Working backward:
- Start from the end, each LEN[i] initially 1.
- At index of 2:
    It can connect to 5, 3, 7, 101, 18
    Longest extension gives length 4.
- Final LEN array gives maximum = 4.

Time Complexity: O(n^2)
- Two nested loops.

Space Complexity: O(n)
- We store an array of size n.
"""

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LEN = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LEN[i] = max(LEN[i], LEN[j] + 1)

        return max(LEN)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Expected: 4
    print(sol.lengthOfLIS([0,1,0,3,2,3]))         # Expected: 4
    print(sol.lengthOfLIS([7,7,7,7,7]))           # Expected: 1