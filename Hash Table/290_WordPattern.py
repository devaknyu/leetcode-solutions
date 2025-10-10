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