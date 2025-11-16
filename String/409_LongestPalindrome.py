class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for char in s:
            if char in seen:
                seen.remove(char)
                res += 2
            else:
                seen.add(char)
        
        if seen:
            res += 1
        
        return res
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        "abccccdd",    # → 7 ("dccaccd")
        "a",           # → 1 ("a")
        "bb",          # → 2 ("bb")
        "abc",         # → 1 ("a")
        "aaa",         # → 3 ("aaa")
    ]
    
    for s in test_cases:
        print(f"Input:  '{s}'")
        result = sol.longestPalindrome(s)
        print(f"Output: {result}\n")