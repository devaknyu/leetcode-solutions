"""
LeetCode 5: Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Problem Description:
- Given a string `s`, return the longest palindromic substring in `s`.
- A palindrome is a string that reads the same forward and backward.

Examples:
s = "babad" → "bab" or "aba"
s = "cbbd"  → "bb"

Approach (Expand Around Center):

Key Insight:
- Every palindrome expands from its center.
- A palindrome can have:
    1) Odd length  → center at a single character (e.g., "aba")
    2) Even length → center between two characters (e.g., "abba")

For each index `i`, we:
1. Expand around (i, i)      → odd-length palindrome
2. Expand around (i, i + 1)  → even-length palindrome

During expansion:
- Move left pointer `l` backward.
- Move right pointer `r` forward.
- Continue while:
      l >= 0
      r < len(s)
      s[l] == s[r]

At each valid expansion:
- If current palindrome length (r - l + 1) is greater than `resLen`,
  update:
      res = s[l:r+1]
      resLen = r - l + 1

We repeat this for every index.

Example:
s = "babad"

At i = 1:
Odd expansion → "bab"
Even expansion → no match

At i = 2:
Odd expansion → "aba"

Longest result = "bab" (or "aba")

Time Complexity: O(n^2)
- For each character, we may expand up to O(n).

Space Complexity: O(1)
- Only a few variables are used.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):

            # Odd-length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even-length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # Expected: "bab" or "aba"
    print(sol.longestPalindrome("cbbd"))   # Expected: "bb"