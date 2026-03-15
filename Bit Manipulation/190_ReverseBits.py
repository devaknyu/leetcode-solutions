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

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (43261596, 964176192),
        (0, 0),
        (1, 2147483648)
    ]

    for n, expected in test_cases:
        result = solution.reverseBits(n)
        status = "✓" if result == expected else "✗"
        print(f"n = {n} → reversed = {result} (Expected: {expected}) {status}")