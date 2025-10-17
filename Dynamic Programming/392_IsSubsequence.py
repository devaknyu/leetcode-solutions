"""
LeetCode 392: Is Subsequence
https://leetcode.com/problems/is-subsequence/

Approach:
- The goal is to check if string `s` is a **subsequence** of string `t`.
- A subsequence means all characters of `s` appear in `t` **in the same order**, but not necessarily consecutively.
- Use a **two-pointer approach**:
  - Pointer `i` tracks the position in `s` (the subsequence to match).
  - Pointer `j` tracks the position in `t` (the main string).
- Iterate through both strings:
  - If `s[i] == t[j]`, move `i` forward (we found a matching character).
  - Always move `j` forward to continue scanning `t`.
- When the loop ends:
  - If `i == len(s)`, it means all characters of `s` were matched in order within `t`.
  - Otherwise, return False.

Example:
s = "abc", t = "ahbgdc" → True  
s = "axc", t = "ahbgdc" → False  

Time Complexity: O(n + m)
Space Complexity: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == len(s) else False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))  # Expected output: True
    print(sol.isSubsequence("axc", "ahbgdc"))  # Expected output: False
    print(sol.isSubsequence("", "ahbgdc"))     # Expected output: True (empty string is always a subsequence)