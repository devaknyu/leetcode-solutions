"""
LeetCode 268: Missing Number
https://leetcode.com/problems/missing-number/

Approach:
- We are given an array containing `n` distinct numbers taken from the range [0, n].
- This means exactly **one number from the range is missing**.
- The goal is to find the missing number.

Key Observations:
- The array length is `n`, but the numbers are from `0` to `n`.
- Therefore, there should be `n + 1` total numbers, meaning one number is missing.

Example:
nums = [3, 0, 1]

Range should be:
[0, 1, 2, 3]

Missing number = 2

Key Idea:
Instead of computing full sums separately, we maintain a running balance.

We initialize:
res = n

Then for each index i:
res += i - nums[i]

Explanation:
- We add the expected index value `i`
- We subtract the actual value `nums[i]`
- At the end, the imbalance reveals the missing number.

Example Walkthrough:

nums = [3,0,1]
n = 3

Start:
res = 3

i=0:
res += 0 - 3 → res = 0

i=1:
res += 1 - 0 → res = 1

i=2:
res += 2 - 1 → res = 2

Missing number = 2

Technique: Mathematical Difference / Running Balance

Algorithm:
1. Initialize result as `res = n`
2. Iterate through the array indices
3. Add the index `i` and subtract the element `nums[i]`
4. The final result will be the missing number

Time Complexity:
- Single pass through array
- Time Complexity: O(n)

Space Complexity:
- Only one variable used
- Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums):
        """
        Returns the missing number in the range [0, n].
        """

        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9,6,4,2,3,5,7,0,1], 8),
        ([0], 1)
    ]

    for nums, expected in test_cases:
        result = solution.missingNumber(nums)
        status = "✓" if result == expected else "✗"
        print(f"nums = {nums} → missing = {result} (Expected: {expected}) {status}")
