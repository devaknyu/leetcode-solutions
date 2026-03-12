"""
LeetCode 136: Single Number
https://leetcode.com/problems/single-number/

Approach:
- We are given an integer array where:
  * Every element appears exactly twice
  * Except for one element which appears only once
- The goal is to find the element that appears only once.

Key Observations:
- XOR has special properties that make this problem very efficient:
  1. a ^ a = 0   (any number XOR itself becomes 0)
  2. a ^ 0 = a   (any number XOR 0 remains unchanged)
  3. XOR is commutative and associative
     meaning order does not matter.

- Because every number appears twice:
  * Duplicate numbers cancel each other out using XOR
  * The only number left after all XOR operations
    will be the number that appears once.

Example:
nums = [4, 1, 2, 1, 2]

Step-by-step XOR:
res = 0
res ^ 4 = 4
res ^ 1 = 5
res ^ 2 = 7
res ^ 1 = 6
res ^ 2 = 4

Final result = 4

Technique: Bit Manipulation (XOR)

Algorithm:
1. Initialize a variable `res = 0`
2. Iterate through each number in the array
3. XOR the current number with `res`
4. Return the final value of `res`

Time Complexity:
- We iterate through the array once
- Time Complexity: O(n)

Space Complexity:
- Only one variable is used
- Space Complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums):
        """
        Returns the element that appears only once
        while all others appear exactly twice.
        """

        res = 0

        # XOR every number in the array
        for n in nums:
            res = res ^ n

        # The remaining value is the single number
        return res

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([7, 3, 5, 3, 5], 7),
    ]

    for nums, expected in test_cases:
        result = solution.singleNumber(nums)
        status = "✓" if result == expected else "✗"
        print(f"nums = {nums} → single number = {result} (Expected: {expected}) {status}")