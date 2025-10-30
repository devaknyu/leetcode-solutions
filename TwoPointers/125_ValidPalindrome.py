
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