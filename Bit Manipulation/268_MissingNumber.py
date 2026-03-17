class Solution:
    def missingNumber(self, nums):
        """
        Returns the missing number in the range [0, n].
        """

        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res
