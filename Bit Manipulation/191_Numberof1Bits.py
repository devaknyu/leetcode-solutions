class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Returns the number of '1' bits in the binary representation of n.
        """

        res = 0

        # Each iteration removes the lowest set bit
        while n:
            n &= n - 1
            res += 1

        return res