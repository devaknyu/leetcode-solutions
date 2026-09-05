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