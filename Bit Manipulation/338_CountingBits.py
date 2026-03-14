"""
LeetCode 338: Counting Bits
https://leetcode.com/problems/counting-bits/

Approach:
- We are given an integer `n`.
- For every number `i` from 0 to `n`, we must compute the number of 1s
  in its binary representation.
- The result should be returned as an array where:
    result[i] = number of set bits in i

Key Observations:
- Binary numbers follow repeating patterns around powers of two.

Example:
0  -> 0
1  -> 1
2  -> 10
3  -> 11
4  -> 100
5  -> 101
6  -> 110
7  -> 111
8  -> 1000

Notice something important:

Numbers after a power of two reuse previous results.

Example around 4:

4 = 100  -> 1 + bits(0)
5 = 101  -> 1 + bits(1)
6 = 110  -> 1 + bits(2)
7 = 111  -> 1 + bits(3)

So:
bits[i] = 1 + bits[i - offset]

Where:
offset = largest power of two ≤ i

Example:
i = 6
offset = 4
6 - 4 = 2

bits[6] = 1 + bits[2]

Technique: Dynamic Programming + Binary Pattern Observation

Algorithm:
1. Create a DP array of size (n + 1)
2. Maintain a variable `offset` that stores the most recent power of two
3. If `i` becomes the next power of two, update `offset`
4. Use the relation:
       dp[i] = 1 + dp[i - offset]
5. Return the DP array

Example Walkthrough (n = 5):

i=0 → 0

i=1 (offset=1)
dp[1] = 1 + dp[0] = 1

i=2 (new power of two → offset=2)
dp[2] = 1 + dp[0] = 1

i=3
dp[3] = 1 + dp[1] = 2

i=4 (new power of two → offset=4)
dp[4] = 1 + dp[0] = 1

i=5
dp[5] = 1 + dp[1] = 2

Result:
[0,1,1,2,1,2]

Time Complexity:
- We iterate once from 1 → n
- Time Complexity: O(n)

Space Complexity:
- DP array of size n+1
- Space Complexity: O(n)
"""

class Solution:
    def countBits(self, n: int):
        """
        Returns an array where index i contains
        the number of set bits in integer i.
        """

        dp = [0] * (n + 1)

        # Tracks the most recent power of two
        offset = 1

        for i in range(1, n + 1):

            # When we hit the next power of two
            if offset * 2 == i:
                offset = i

            # Use the DP relation
            dp[i] = 1 + dp[i - offset]

        return dp

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (0, [0]),
    ]

    for n, expected in test_cases:
        result = solution.countBits(n)
        status = "✓" if result == expected else "✗"
        print(f"n = {n} → {result} (Expected: {expected}) {status}")