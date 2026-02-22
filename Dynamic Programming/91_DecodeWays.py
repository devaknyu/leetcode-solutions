"""
LeetCode 91: Decode Ways
https://leetcode.com/problems/decode-ways/

Problem Description:
- A message containing letters from A–Z is encoded using numbers:
      'A' -> 1
      'B' -> 2
      ...
      'Z' -> 26
- Given a string `s` containing only digits, return the number of ways to decode it.
- Leading zeros are invalid.
- "0" cannot be decoded by itself.

Examples:
s = "12"   → 2
Explanation: "AB" (1 2) or "L" (12)

s = "226"  → 3
Explanation: "BZ" (2 26), "VF" (22 6), "BBF" (2 2 6)

s = "06"   → 0
Explanation: No valid decoding.

Approach (Bottom-Up Dynamic Programming):

Key Idea:
- Let dp[i] represent the number of ways to decode substring s[i:].
- We build the solution from right to left.

Base Case:
- dp[len(s)] = 1
  (Empty string has one valid decoding way.)

Transition Rules:

1) If s[i] == "0":
   - Cannot decode a single zero.
   - dp[i] = 0

2) Otherwise:
   - We can decode one digit:
       dp[i] = dp[i+1]

3) Additionally, if two-digit number is valid (10–26):
   - Add dp[i+2]

Valid two-digit condition:
    s[i] == "1"
    OR
    s[i] == "2" AND s[i+1] in "0123456"

Example:
s = "226"

Initialize:
dp[3] = 1

i = 2 ("6"):
dp[2] = dp[3] = 1

i = 1 ("2"):
Single digit → dp[2] = 1
Two digits "26" valid → + dp[3] = 1
dp[1] = 2

i = 0 ("2"):
Single digit → dp[1] = 2
Two digits "22" valid → + dp[2] = 1
dp[0] = 3

Return dp[0] = 3

Time Complexity: O(n)
- Single pass through the string.

Space Complexity: O(n)
- Dictionary stores dp values for each index.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                dp[i] += dp[i + 2]

        return dp[0]
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))   # Expected: 2
    print(sol.numDecodings("226"))  # Expected: 3
    print(sol.numDecodings("06"))   # Expected: 0
