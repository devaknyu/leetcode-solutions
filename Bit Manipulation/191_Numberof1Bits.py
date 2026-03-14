"""
LeetCode 191: Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Approach:
- We are given an unsigned integer `n`.
- The goal is to count how many '1' bits exist in its binary representation.
- This count is also known as the **Hamming Weight**.

Key Observations:
- A naive approach would check every bit using shifting.
- However, there is a very efficient trick using the operation:

    n & (n - 1)

- This operation removes the **rightmost set bit (1)** from the number.

Example:
n = 13

Binary representation:
13 = 1101

Step-by-step:

1101  (13)
1100  (13 - 1)
----
1100  -> removes rightmost 1

Next:

1100
1011
----
1000

Next:

1000
0111
----
0000

We removed **3 set bits**, so the Hamming Weight = 3.

Key Insight:
- Each iteration removes **one set bit**
- Therefore, the number of loop iterations equals the number of 1s.

Technique: Bit Manipulation (Brian Kernighan’s Algorithm)

Algorithm:
1. Initialize counter `res = 0`
2. While `n` is not zero:
   - Perform `n = n & (n - 1)` to remove the lowest set bit
   - Increment the counter
3. Return the counter

Time Complexity:
- O(k), where k = number of set bits
- In the worst case (all bits are 1), this becomes O(32) for a 32-bit integer

Space Complexity:
- O(1) constant extra space
"""

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
