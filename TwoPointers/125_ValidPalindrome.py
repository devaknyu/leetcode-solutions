"""
LeetCode 125: Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Approach:
- Given a string `s`, determine if it reads the same forward and backward,
  considering only alphanumeric characters and ignoring cases.
- The challenge is to ignore spaces, punctuation, and symbols.

Steps:
1. Use two pointers — `left` and `right` — starting at the beginning and end of the string.
2. Move each pointer inward until both point to alphanumeric characters.
3. Compare the lowercase versions of the characters.
   - If they differ, return False immediately.
4. Continue until `left` >= `right`.
5. If all checks pass, return True.

Helper Function:
- `AlphaNum(c)` checks whether a character is alphanumeric using ASCII ranges.

Example:
Input:
  s = "A man, a plan, a canal: Panama"
Output:
  True
Explanation:
  After removing non-alphanumeric and ignoring case → "amanaplanacanalpanama" is a palindrome.

Input:
  s = "race a car"
Output:
  False

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = list(s)
        left = 0
        right = len(char) - 1
        
        while left < right:
            while left < right and not self.AlphaNum(char[left]):
                left += 1
            while left < right and not self.AlphaNum(char[right]):
                right -= 1
            if char[left].lower() != char[right].lower():
                return False
            left += 1
            right -= 1
        
        return True

    def AlphaNum(self, c: str) -> bool:
        return (ord('0') <= ord(c) <= ord('9')) or (ord('a') <= ord(c.lower()) <= ord('z'))
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Expected output: True
    print(sol.isPalindrome("race a car"))                      # Expected output: False
    print(sol.isPalindrome(" "))                               # Expected output: True