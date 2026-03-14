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

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (11, 3),   # 1011
        (128, 1),  # 10000000
        (2147483645, 30)
    ]

    for n, expected in test_cases:
        result = solution.hammingWeight(n)
        status = "✓" if result == expected else "✗"
        print(f"n = {n} → set bits = {result} (Expected: {expected}) {status}")
