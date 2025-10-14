"""
LeetCode 70: Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

Approach:
- You are climbing a staircase with `n` steps.
- Each time, you can climb either **1 step** or **2 steps**.
- The goal is to find the total number of distinct ways to reach the top.
- This is a **Fibonacci-like problem**, because:
  - To reach step `n`, you can come from step `n-1` (taking 1 step) or step `n-2` (taking 2 steps).
  - So, `ways(n) = ways(n-1) + ways(n-2)`
- Use two variables (`one`, `two`) to store the previous two computed values:
  - `one` → number of ways to reach the current step.
  - `two` → number of ways to reach the previous step.
- Iterate `n-1` times and update the values iteratively to avoid recursion and extra space.

Example:
n = 2 → [ (1+1), (2) ] → 2  
n = 3 → [ (1+1+1), (1+2), (2+1) ] → 3  

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # Expected output: 2
    print(sol.climbStairs(3))  # Expected output: 3
    print(sol.climbStairs(5))  # Expected output: 8