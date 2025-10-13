"""
LeetCode 383: Ransom Note
https://leetcode.com/problems/ransom-note/

Approach:
- The goal is to determine if the `ransomNote` can be constructed using the letters from `magazine`.
- Each letter in `magazine` can only be used once.
- Use a hash map (dictionary) `available` to count the frequency of each character in `magazine`.
- Iterate through each character in `ransomNote`:
  - If the character doesn’t exist in `available`, return False (not enough letters).
  - Otherwise, decrement its count. If the count becomes zero, remove it from the dictionary.
- If all characters in `ransomNote` can be matched, return True.

Example:
ransomNote = "a", magazine = "b" → False  
ransomNote = "aa", magazine = "ab" → False  
ransomNote = "aa", magazine = "aab" → True  

Time Complexity: O(n + m)
Space Complexity: O(m)
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = {}
        for c in magazine:
            if c in available:
                available[c] += 1
            else:
                available[c] = 1
        
        for c in ransomNote:
            if c not in available:
                return False
            elif available[c] == 1:
                del available[c]
            else:
                available[c] -= 1
        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b"))        # Expected output: False
    print(sol.canConstruct("aa", "ab"))      # Expected output: False
    print(sol.canConstruct("aa", "aab"))     # Expected output: True