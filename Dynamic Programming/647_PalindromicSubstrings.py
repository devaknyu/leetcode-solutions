"""
LeetCode 647: Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Problem Description:
- Given a string `s`, return the number of palindromic substrings in it.
- A substring is a contiguous sequence of characters.
- A palindrome reads the same forward and backward.
- Every single character counts as a palindrome.

Examples:
s = "abc"   → 3
Explanation: "a", "b", "c"

s = "aaa"   → 6
Explanation: "a", "a", "a", "aa", "aa", "aaa"

Approach (Expand Around Center):

Key Insight:
- Every palindrome expands from its center.
- Just like LeetCode 5, we consider:
    1) Odd-length palindromes  → center at (i, i)
    2) Even-length palindromes → center at (i, i+1)

Instead of tracking the longest substring,
we count how many valid palindromes we find.

Helper Function:
countPal(s, l, r)
- Expands while:
      l >= 0
      r < len(s)
      s[l] == s[r]
- Each valid expansion adds 1 to the result.
- Returns the total palindromes centered at (l, r).

Main Logic:
- For each index i:
    res += countPal(s, i, i)      # Odd-length palindromes
    res += countPal(s, i, i + 1)  # Even-length palindromes

Example:
s = "aaa"

i = 0:
Odd  → "a"
Even → "aa"

i = 1:
Odd  → "a", "aaa"
Even → "aa"

i = 2:
Odd  → "a"

Total = 6

Time Complexity: O(n^2)
- For each character, expansion can take O(n).

Space Complexity: O(1)
- No extra data structures used.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPal(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        res = 0
        for i in range(len(s)):
            res += countPal(s, i, i)      # Odd-length
            res += countPal(s, i, i + 1)  # Even-length

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))  # Expected: 3
    print(sol.countSubstrings("aaa"))  # Expected: 6
