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
