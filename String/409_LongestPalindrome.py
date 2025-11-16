"""
LeetCode 409: Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

Approach:
- A palindrome can have at most one character with odd frequency
- All other characters must have even frequency
- Use set to track pairs of characters

Technique: Character Pair Counting with Set
1. Track characters in a set
2. When we see a character already in set, we found a pair
3. Remove from set and add 2 to result (for the pair)
4. If set has any characters left at end, add 1 (for middle character)

Time Complexity: O(n)
Space Complexity: O(1) - set size limited to 52 (letters)
"""

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