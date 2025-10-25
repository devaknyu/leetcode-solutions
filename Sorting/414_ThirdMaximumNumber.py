"""
LeetCode 414: Third Maximum Number
https://leetcode.com/problems/third-maximum-number/

Approach:
- We need to find the **third distinct maximum number** in the list.
- If the third maximum does not exist, return the **maximum number**.

Steps:
1. Convert the list `nums` into a `set` to remove duplicates.
2. Sort the unique numbers in **descending order**.
3. If there are at least three distinct numbers, return the third one.
4. Otherwise, return the first (largest) number.

Example:
Input:
  nums = [3, 2, 1]
Output:
  1
Explanation:
  The distinct numbers are [3, 2, 1], and the third maximum is 1.

Input:
  nums = [1, 2]
Output:
  2
Explanation:
  There is no third distinct number, so we return the maximum (2).

Time Complexity: O(n log n) — due to sorting
Space Complexity: O(n) — for the set of unique elements
"""

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        sorted_nums = sorted(unique_nums, reverse=True)

        if len(sorted_nums) > 2:
            return sorted_nums[2]
        else:
            return sorted_nums[0]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.thirdMax([3, 2, 1]))         # Expected output: 1
    print(sol.thirdMax([1, 2]))            # Expected output: 2
    print(sol.thirdMax([2, 2, 3, 1]))      # Expected output: 1
    print(sol.thirdMax([5, 7, 7, 7, 8]))   # Expected output: 8
