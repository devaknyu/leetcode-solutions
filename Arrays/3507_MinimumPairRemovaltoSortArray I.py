"""
LeetCode 3507: Minimum Pair Removal to Sort Array I
https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

Approach:
- We are given an array of integers and can repeatedly perform a forced operation:
  * Select the adjacent pair with the minimum sum (leftmost if tie)
  * Replace the pair with their sum
- The goal is to find the minimum number of such operations needed
  to make the array non-decreasing.

Key Observations:
- The choice of pair is NOT flexible; it is strictly defined by the problem.
- Therefore, this is a greedy simulation problem.
- At each step, we must:
  1. Check if the array is already non-decreasing
  2. Find the adjacent pair with the minimum sum
  3. Replace that pair with their sum
  4. Count the operation

Technique: Greedy + Array Simulation
1. Repeatedly simulate the operation until the array becomes non-decreasing
2. Use a helper function to check sorted condition
3. Linearly scan adjacent pairs to find the minimum sum (leftmost in case of ties)
4. Replace the pair using array slicing

Time Complexity:
- Each operation takes O(n) to scan adjacent pairs
- In the worst case, up to O(n) operations
- Overall Time Complexity: O(n^2)

Space Complexity:
- O(n) due to array reconstruction during simulation
"""

class Solution:
    def minimumOperations(self, nums):
        """
        Returns the minimum number of operations needed
        to make the array non-decreasing.
        """

        # Helper function to check if array is non-decreasing
        def is_non_decreasing(arr):
            # all() returns True if all comparisons are True
            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

        operations = 0

        # Continue until array becomes non-decreasing
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            min_index = 0

            # Find the leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_index = i

            # Replace the chosen pair with their sum
            nums = nums[:min_index] + [min_sum] + nums[min_index + 2:]

            # Count this operation
            operations += 1

        return operations

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 1, 2], 1),
        ([1, 2, 3], 0),
        ([5, 2, 1], 2),
        ([10, 1, 2, 9], 1),
    ]

    for nums, expected in test_cases:
        result = solution.minimumOperations(nums[:])  # copy to preserve original
        status = "✓" if result == expected else "✗"
        print(f"nums = {nums} → operations = {result} (Expected: {expected}) {status}")