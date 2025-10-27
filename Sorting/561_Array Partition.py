"""
LeetCode 561: Array Partition
https://leetcode.com/problems/array-partition/

Approach:
- Given an integer array `nums` of 2n elements, we need to pair them up into n pairs (a1, b1), (a2, b2), …  
  such that the **sum of the minimum values in each pair** is maximized.
- Intuition:
  - Sorting the array ensures that elements close in value are paired together.
  - Pairing adjacent numbers minimizes the loss between large and small numbers.
  - Therefore, the optimal strategy is to sum up every **even-indexed element** (0-based index) after sorting.

Steps:
1. Sort the array in ascending order.
2. Iterate through the array, stepping by 2.
3. Add every first element of each pair (index 0, 2, 4, …) to the result.
4. Return the final sum.

Example:
Input:
  nums = [1, 4, 3, 2]
Output:
  4
Explanation:
  After sorting → [1, 2, 3, 4]
  Pairing → (1,2), (3,4)
  Sum of min values → 1 + 3 = 4

Time Complexity: O(n log n) — for sorting
Space Complexity: O(1)
"""

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        result = 0

        for i in range(0, len(sorted_nums), 2):
            result += sorted_nums[i]
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayPairSum([1, 4, 3, 2]))     # Expected output: 4
    print(sol.arrayPairSum([6, 2, 6, 5, 1, 2]))  # Expected output: 9
    print(sol.arrayPairSum([1, 1, 1, 1]))     # Expected output: 2