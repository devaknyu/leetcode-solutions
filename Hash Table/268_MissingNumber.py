"""
LeetCode 268: Missing Number
https://leetcode.com/problems/missing-number/

Approach:
- The array `nums` contains `n` distinct numbers from the range `[0, n]`, but one number is missing.
- Initialize a result variable `res` as `len(nums)` to include the possible missing number `n`.
- For each index `i`, add `i - nums[i]` to `res`.  
  This effectively calculates the difference between the expected sum of indices and the actual sum of numbers.
- After the loop, `res` will hold the missing number.

Example:
nums = [3, 0, 1]
Expected total = 0 + 1 + 2 + 3 = 6
Actual total = 3 + 0 + 1 = 4
Missing = 6 - 4 = 2

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))  # Expected output: 2
    print(sol.missingNumber([0, 1]))     # Expected output: 2
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))  # Expected output: 8