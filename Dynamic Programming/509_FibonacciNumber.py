"""
LeetCode 509: Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

Approach:
- The Fibonacci sequence is defined as:
  F(0) = 0, F(1) = 1  
  F(n) = F(n - 1) + F(n - 2) for n > 1
- This recursive approach directly applies the mathematical definition.
- Base cases:
  - If n == 0 → return 0
  - If n == 1 → return 1
- For n > 1, recursively calculate F(n - 1) and F(n - 2) and return their sum.
- While simple and intuitive, this method has exponential time complexity due to repeated calculations.

Example:
n = 4 → F(4) = F(3) + F(2) = (F(2) + F(1)) + (F(1) + F(0)) = 3  

Time Complexity: O(2^n)
Space Complexity: O(n) (due to recursive call stack)
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            a = self.fib(n - 1)
            b = self.fib(n - 2)
            return a + b

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(0))  # Expected output: 0
    print(sol.fib(1))  # Expected output: 1
    print(sol.fib(4))  # Expected output: 3
    print(sol.fib(5))  # Expected output: 5