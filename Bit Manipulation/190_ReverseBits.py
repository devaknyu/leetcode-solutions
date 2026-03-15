class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverses the bits of a 32-bit unsigned integer.
        """

        res = 0

        # Iterate through all 32 bits
        for i in range(32):

            # Extract the i-th bit
            bit = (n >> i) & 1

            # Place it in the reversed position
            res = res | (bit << (31 - i))

        return res
