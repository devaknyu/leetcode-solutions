"""
LeetCode 290: Word Pattern
https://leetcode.com/problems/word-pattern/

Approach:
- We are given a pattern string and a space-separated string `s`.
- The goal is to check if there exists a **one-to-one mapping** between each character in `pattern` 
  and each word in `s`.
- Split `s` into individual words using `split(" ")`.
- If the lengths of `pattern` and `words` differ, return False immediately.
- Use two hash maps (dictionaries):
  - `charToWord` maps characters in the pattern to words.
  - `wordToChar` maps words to characters in the pattern.
- Iterate through both `pattern` and `words` simultaneously:
  - If a character or word has been mapped before, ensure the existing mapping is consistent.
  - If not, create a new mapping.
- If all mappings are consistent, return True.

Example:
pattern = "abba", s = "dog cat cat dog" → True  
pattern = "abba", s = "dog cat cat fish" → False  
pattern = "aaaa", s = "dog cat cat dog" → False  
pattern = "abba", s = "dog dog dog dog" → False  

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        wordToChar = {}
        charToWord = {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            
            charToWord[c] = w
            wordToChar[w] = c
        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))   # Expected output: True
    print(sol.wordPattern("abba", "dog cat cat fish"))  # Expected output: False
    print(sol.wordPattern("aaaa", "dog cat cat dog"))   # Expected output: False
    print(sol.wordPattern("abba", "dog dog dog dog"))   # Expected output: False