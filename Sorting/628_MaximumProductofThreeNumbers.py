"""
LeetCode 628: Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/

Approach:
- Given an integer array `nums`, find three numbers whose product is maximum.
- The maximum product can come from one of two cases:
  1. The **three largest numbers** (if all are positive or large).
  2. The **two smallest (possibly negative) numbers and the largest number** 
     — since two negatives make a positive.

Steps:
1. Sort the array in descending order.
2. Compute:
   - product1 = nums[0] * nums[1] * nums[2]  (top three largest numbers)
   - product2 = nums[0] * nums[-1] * nums[-2] (largest * two smallest)
3. Return the maximum of the two.

Example:
Input:
  nums = [1, 2, 3]
Output:
  6
Explanation:
  1 * 2 * 3 = 6

Input:
  nums = [-10, -10, 5, 2]
Output:
  500
Explanation:
  (-10) * (-10) * 5 = 500

Time Complexity: O(n log n) — due to sorting
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        product = max(
            sorted_nums[0] * sorted_nums[1] * sorted_nums[2],
            sorted_nums[0] * sorted_nums[-1] * sorted_nums[-2]
        )
        return product
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumProduct([1, 2, 3]))            # Expected output: 6
    print(sol.maximumProduct([1, 2, 3, 4]))         # Expected output: 24
    print(sol.maximumProduct([-10, -10, 5, 2]))     # Expected output: 500
    print(sol.maximumProduct([-1, -2, -3]))         # Expected output: -6