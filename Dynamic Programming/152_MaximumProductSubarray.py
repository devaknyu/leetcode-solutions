"""
LeetCode 152: Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Problem Description:
- Given an integer array `nums`, find the contiguous subarray
  (containing at least one number) which has the largest product.
- Return the product.

Examples:
nums = [2, 3, -2, 4] → 6
Explanation: [2, 3] has the largest product.

nums = [-2, 0, -1] → 0
Explanation: The result cannot be 2 because [-2, -1] is not contiguous.

Key Challenge:
- Unlike maximum sum subarray (Kadane’s algorithm),
  negative numbers complicate things.
- A negative number can turn:
    - A large positive product → negative
    - A large negative product → positive

Therefore, we must track BOTH:
    1) Current maximum product
    2) Current minimum product

Approach (Dynamic Programming – Track Max and Min):

At each index:
- numMax → maximum product ending at current index
- numMin → minimum product ending at current index
  (important because multiplying by negative can flip signs)

Why track numMin?
Example:
nums = [-2, 3, -4]

Step-by-step:
- After -2:
    numMax = -2
    numMin = -2
- After 3:
    numMax = 3
    numMin = -6
- After -4:
    numMax = 24   (because -6 * -4 = 24)
    numMin = -12

Without tracking numMin, we would miss the 24.

Algorithm Steps:

1. Initialize:
    res = max(nums)  (handles cases where all numbers are negative)
    numMax = 1
    numMin = 1

2. For each number n:
    tmp = numMax * n   (store before updating)

    numMax = max(numMax * n, numMin * n, n)
    numMin = min(tmp, numMin * n, n)

    res = max(res, numMax)

3. Return res

Time Complexity: O(n)
- Single pass through array.

Space Complexity: O(1)
- Only a few variables used.
"""

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        numMax, numMin = 1, 1

        for n in nums:
            tmp = numMax * n
            numMax = max(numMax * n, numMin * n, n)
            numMin = min(tmp, numMin * n, n)
            res = max(res, numMax)

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))  # Expected: 6
    print(sol.maxProduct([-2, 0, -1]))    # Expected: 0
    print(sol.maxProduct([-2, 3, -4]))    # Expected: 24