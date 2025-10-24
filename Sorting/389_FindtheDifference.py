"""
LeetCode 389: Find the Difference
https://leetcode.com/problems/find-the-difference/

Approach:
- We are given two strings `s` and `t`, where `t` is formed by shuffling `s` and adding one extra character.
- The task is to find that extra character.

Steps:
1. Convert each character to its ASCII value using the `ord()` function.
2. Compute the sum of ASCII values of all characters in `s` and in `t`.
3. The difference `sum_T - sum_S` will give the ASCII value of the extra character.
4. Convert it back to a character using `chr()`.

Example:
Input:
  s = "abcd"
  t = "abcde"
Output:
  "e"
Explanation:
  ASCII sum of `t` - ASCII sum of `s` = ord('e').

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_S, sum_T = 0, 0
        for i in s:
            sum_S += ord(i)
        for i in t:
            sum_T += ord(i)
        return chr(sum_T - sum_S)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))  # Expected output: "e"
    print(sol.findTheDifference("", "y"))           # Expected output: "y"
    print(sol.findTheDifference("a", "aa"))         # Expected output: "a"