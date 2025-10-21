"""
LeetCode 1137: N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/

Approach:
- The Tribonacci sequence is similar to Fibonacci, but each term is the sum of the previous three:
  T(n) = T(n-1) + T(n-2) + T(n-3)
- Base cases:
  T(0) = 0, T(1) = 1, T(2) = 1
- We can use a rolling array of size 3 to store the last three computed values.
- For each step, we update the array to hold the next value.

Steps:
1. Initialize `t = [0, 1, 1]` representing T(0), T(1), and T(2).
2. If `n < 3`, return `t[n]` directly.
3. For i from 3 to n:
   - Compute the next term as the sum of all elements in `t`.
   - Shift the array: t[0] = t[1], t[1] = t[2], t[2] = new term.
4. Return t[2] as the nth Tribonacci number.

Time Complexity: O(n)
Space Complexity: O(1)

Example:
n = 4 → Output: 4  (since 0, 1, 1, 2, 4)
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]

        if n < 3:
            return t[n]

        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
        return t[2]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci(4))   # Expected output: 4
    print(sol.tribonacci(25))  # Expected output: 1389537
    print(sol.tribonacci(0))   # Expected output: 0