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