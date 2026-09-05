class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        char_set = set()
        
        for r in range(len(s)):
            # Shrink window from left until no duplicate
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # Current window size
            window_size = r - l + 1
            longest = max(longest, window_size)
            # Add current character to set
            char_set.add(s[r])
            
        return longest

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ("abcabcbb", 3),     # "abc"
        ("bbbbb", 1),        # "b"
        ("pwwkew", 3),       # "wke"
        ("", 0),             # empty string
        (" ", 1),            # single space
        ("au", 2),           # "au"
        ("dvdf", 3),         # "vdf"
    ]
    
    for s, expected in test_cases:
        result = sol.lengthOfLongestSubstring(s)
        status = "✓" if result == expected else "✗"
        print(f"'{s}' → {result} (Expected: {expected}) {status}")
    
    # Visual demonstration
    print("\n" + "="*50)
    print("Visual demonstration for 'abcabcbb':")
    demo_string = "abcabcbb"
    print(f"String: {demo_string}")
    
    # Show the sliding window process
    l = 0
    char_set = set()
    for r in range(len(demo_string)):
        while demo_string[r] in char_set:
            char_set.remove(demo_string[l])
            l += 1
        char_set.add(demo_string[r])
        window = demo_string[l:r+1]
        print(f"Window [{l},{r}]: '{window}' (length: {r-l+1})")
    
    final_result = sol.lengthOfLongestSubstring(demo_string)
    print(f"\nLongest substring without repeating characters: {final_result}")
