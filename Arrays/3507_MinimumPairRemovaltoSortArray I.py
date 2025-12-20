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