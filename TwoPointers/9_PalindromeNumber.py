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
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        121,     # → True
        -121,    # → False
        10,      # → False
        0,       # → True
        12321,   # → True
        12345,   # → False
    ]
    
    for x in test_cases:
        print(f"Input:  {x}")
        result = sol.isPalindrome(x)
        print(f"Output: {result}\n")