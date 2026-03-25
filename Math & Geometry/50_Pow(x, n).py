"""
LeetCode 50: Pow(x, n)
https://leetcode.com/problems/powx-n/

Approach:
- We are given a number `x` and an integer `n`.
- The goal is to compute:
        x^n

- A naive approach would multiply `x` n times → O(n)
- This is too slow for large `n`.

Key Observations:
- We can use **Exponentiation by Squaring** to reduce complexity.

Core Idea:
- Break the problem into smaller subproblems:

If n is even:
    x^n = (x^(n/2))^2

If n is odd:
    x^n = x * (x^(n//2))^2

This reduces the problem size by half each time.

Example:

x = 2, n = 10

2^10 = (2^5)^2
2^5  = 2 * (2^2)^2
2^2  = (2^1)^2
2^1  = 2

Build back up:
2^2 = 4
2^5 = 2 * 4^2 = 32
2^10 = 32^2 = 1024

Handling Negative Powers:
- If n < 0:
    x^(-n) = 1 / x^n

Technique: Divide & Conquer (Binary Exponentiation)

Algorithm:
1. Define recursive helper(x, n)
2. Base cases:
   - x == 0 → return 0
   - n == 0 → return 1
3. Recursively compute:
       half = helper(x, n//2)
4. Square result:
       res = half * half
5. If n is odd → multiply by x
6. Handle negative exponent at the end

Time Complexity:
- Each step halves n
- Time Complexity: O(log n)

Space Complexity:
- Recursion stack
- Space Complexity: O(log n)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Computes x raised to the power n.
        """

        def helper(x, n):

            if x == 0:
                return 0

            if n == 0:
                return 1

            # Divide step
            res = helper(x, n // 2)

            # Conquer step (square)
            res = res * res

            # If n is odd, multiply one extra x
            return x * res if n % 2 else res

        # Handle negative exponent
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
    
# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (0.0, 5, 0.0),
    ]

    for x, n, expected in test_cases:
        result = solution.myPow(x, n)
        status = "✓" if abs(result - expected) < 1e-5 else "✗"
        print(f"x = {x}, n = {n} → result = {result} (Expected: {expected}) {status}")