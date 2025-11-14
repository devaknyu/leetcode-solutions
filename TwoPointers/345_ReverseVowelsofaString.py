
class Solution:
    def reverseVowels(self, s: str) -> str:
        char = list(s)
        l = 0
        r = len(char) - 1
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])

        while l < r:
            # Find next vowel from left
            while l < r and char[l] not in vowels:
                l += 1
            # Find next vowel from right
            while l < r and char[r] not in vowels:
                r -= 1
            # Swap vowels
            char[l], char[r] = char[r], char[l]
            l += 1
            r -= 1
            
        return ''.join(char)
