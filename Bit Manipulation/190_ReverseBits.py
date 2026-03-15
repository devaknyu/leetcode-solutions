"""
LeetCode 190: Reverse Bits
https://leetcode.com/problems/reverse-bits/

Approach:
- We are given a 32-bit unsigned integer `n`.
- The goal is to reverse its binary bits and return the resulting integer.

Example:
Input:
n = 00000010100101000001111010011100

Output:
964176192

Reversed:
00111001011110000010100101000000

Key Observations:
- Each bit in position `i` in the original number should move to
  position `(31 - i)` in the reversed number.
- We can extract each bit from `n` using right shift and masking.
- Then place that bit in the correct reversed position.

Bit Extraction:
    (n >> i) & 1

Explanation:
- Shift `n` right by `i` bits
- Mask with `& 1` to isolate the last bit

Bit Placement:
    bit << (31 - i)

Explanation:
- Move the extracted bit to its reversed position.

Technique: Bit Manipulation (Shifting + Masking)

Algorithm:
1. Initialize result variable `res = 0`
2. Loop from `i = 0` to `31` (since it's a 32-bit integer)
3. Extract the i-th bit from `n`
4. Place that bit at position `(31 - i)` in `res`
5. Use OR operation to combine it into `res`
6. Return `res`

Example Walkthrough:

n = 5
Binary (32-bit):
00000000000000000000000000000101

Reverse:
10100000000000000000000000000000

Time Complexity:
- Fixed 32 iterations
- Time Complexity: O(1)

Space Complexity:
- Only a few variables used
- Space Complexity: O(1)
"""

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