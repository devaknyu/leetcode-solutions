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

