"""
LeetCode 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/

Approach:
- If the two strings have different lengths, they cannot be anagrams.
- Use two hash maps (dictionaries) to count the frequency of each character in both strings.
- Compare the two maps — if all character counts match, return True; otherwise, return False.

Time Complexity: O(n)
Space Complexity: O(1) — since the alphabet is fixed (only 26 lowercase letters)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # Expected output: True
    print(sol.isAnagram("rat", "car"))          # Expected output: False