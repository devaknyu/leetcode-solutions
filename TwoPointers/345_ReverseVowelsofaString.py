"""
LeetCode 345: Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Approach:
- Reverse only the vowels in the string while keeping consonants in their original positions
- Use two pointers to find vowels from both ends and swap them

Technique: Two-Pointer with Vowel Checking
1. Convert string to list for in-place modification
2. Use left and right pointers starting from both ends
3. Move left pointer until it finds a vowel
4. Move right pointer until it finds a vowel  
5. Swap the vowels and continue until pointers meet

Time Complexity: O(n)
Space Complexity: O(n) for the character list
"""

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
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        "hello",     # → "holle"
        "leetcode",  # → "leotcede"  
        "aA",        # → "Aa"
        "xyz",       # → "xyz"
        "ai"         # → "ia"
    ]
    
    for s in test_cases:
        print(f"Input:  {s}")
        result = sol.reverseVowels(s)
        print(f"Output: {result}\n")