"""
LeetCode 70: Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

Approach:
- At each step, you can climb either 1 or 2 steps
- To reach step n:
    ways(n) = ways(n-1) + ways(n-2)
- This forms a Fibonacci-like recurrence
- Use iterative DP with constant space

Technique: Bottom-Up Dynamic Programming (Fibonacci Pattern)
1. Base cases:
   - 1 step → 1 way
   - 2 steps → 2 ways
2. For each step i:
   - ways(i) = ways(i-1) + ways(i-2)
3. Use two variables to store previous two results

Time Complexity: O(n)
- Single pass loop

Space Complexity: O(1)
- Only two variables used
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [1, 2, 3, 4, 5]

    for n in test_cases:
        result = sol.climbStairs(n)
        print(f"n={n} → {result}")