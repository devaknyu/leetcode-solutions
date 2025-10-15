"""
LeetCode 338: Counting Bits
https://leetcode.com/problems/counting-bits/

Approach:
- The task is to return an array `dp` where `dp[i]` represents the number of 1's (set bits)
  in the binary representation of `i`, for all numbers from 0 to `n`.
- Use **Dynamic Programming (DP)**:
  - Initialize `dp` with size `n + 1`, all zeros.
  - Maintain a variable `offset` which tracks the most recent power of two (1, 2, 4, 8, ...).
- For each number `i` from 1 to `n`:
  - When `i` reaches `offset * 2`, update `offset` to the new power of two.
  - The number of set bits in `i` can be derived as:
    `dp[i] = 1 + dp[i - offset]`
    (because `i - offset` represents the remaining bits after removing the most significant 1-bit).
- This way, we reuse previous computed results efficiently.

Example:
n = 5  
Binary representations:  
0 -> 0, 1 -> 1, 2 -> 10, 3 -> 11, 4 -> 100, 5 -> 101  
Output → [0, 1, 1, 2, 1, 2]

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))  # Expected output: [0, 1, 1]
    print(sol.countBits(5))  # Expected output: [0, 1, 1, 2, 1, 2]
