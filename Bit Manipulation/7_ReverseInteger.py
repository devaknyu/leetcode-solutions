"""
LeetCode 7: Reverse Integer
https://leetcode.com/problems/reverse-integer/

Approach:
- We are given a signed 32-bit integer `x`.
- The goal is to reverse its digits.
- If reversing causes overflow beyond 32-bit signed integer range,
  return 0.

Constraints:
- 32-bit signed integer range:
    [-2^31, 2^31 - 1]
    → [-2147483648, 2147483647]

Key Observations:
- We extract digits from the right using modulo.
- Build the reversed number digit by digit.
- We MUST check for overflow BEFORE updating the result.

Digit Extraction:
    digit = x % 10

In Python, to handle negatives correctly:
    digit = int(math.fmod(x, 10))

Why?
- Python’s `%` behaves differently for negatives.
- `math.fmod` preserves the sign.

Truncating Number:
    x = int(x / 10)

Overflow Check (CRITICAL):
Before doing:
    res = res * 10 + digit

We check:

For positive overflow:
    if res > MAX//10 OR
       (res == MAX//10 AND digit > MAX % 10)

For negative overflow:
    if res < MIN//10 OR
       (res == MIN//10 AND digit < MIN % 10)

Technique: Math + Digit Manipulation + Overflow Handling

Algorithm:
1. Initialize result `res = 0`
2. Extract last digit of `x`
3. Remove last digit from `x`
4. Check if adding digit causes overflow
5. Append digit to result
6. Repeat until `x == 0`
7. Return result

Example:

x = 123

Step-by-step:
res = 0

digit = 3 → res = 3
digit = 2 → res = 32
digit = 1 → res = 321

Result = 321

Negative Example:

x = -123 → result = -321

Overflow Example:

x = 1534236469 → reversed exceeds 32-bit → return 0

Time Complexity:
- O(log10(n)) → number of digits

Space Complexity:
- O(1)
"""


import math

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses digits of a 32-bit signed integer.
        Returns 0 if overflow occurs.
        """

        min_n = -2147483648
        max_n = 2147483647    
        res = 0

        while x:

            # Extract last digit (handles negative correctly)
            digit = int(math.fmod(x, 10))

            # Remove last digit
            x = int(x / 10)

            # Check positive overflow
            if (res > (max_n // 10)) or \
               (res == (max_n // 10) and digit >= max_n % 10):
                return 0
            
            # Check negative overflow
            if (res < (min_n // 10)) or \
               (res == (min_n // 10) and digit <= min_n % 10):
                return 0
            
            # Build reversed number
            res = (res * 10) + digit

        return res

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # overflow case
    ]

    for x, expected in test_cases:
        result = solution.reverse(x)
        status = "✓" if result == expected else "✗"
        print(f"x = {x} → reversed = {result} (Expected: {expected}) {status}")