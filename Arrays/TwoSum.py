"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/

Problem:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Approach:
- Use a brute-force nested loop to check all pairs.
- If nums[i] + nums[j] equals target, return their indices.
- This is the most straightforward solution (not the most efficient).

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

# Example run for local testing
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))  # Output: [0, 1]
