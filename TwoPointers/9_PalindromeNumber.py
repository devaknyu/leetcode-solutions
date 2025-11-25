class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
            
        char = str(x)
        l = 0
        r = len(char) - 1

        while l < r:
            if char[l] != char[r]:
                return False
            l += 1
            r -= 1
        return True