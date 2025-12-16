"""
LeetCode 76: Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Approach:
- Find minimum substring in s that contains all characters of t
- Use sliding window with two hash maps for character counts
- Expand window to include necessary characters, then contract to find minimum

Technique: Sliding Window with Character Counting
1. Create countT: frequency of each character in t
2. Maintain window: frequency of characters in current window
3. Track have: how many characters in t are satisfied in window
4. need: number of unique characters in t
5. Expand right pointer until have == need
6. Contract left pointer to find minimum valid window

Time Complexity: O(|s| + |t|)
Space Complexity: O(|t|) for character frequency maps
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        
        # Count characters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # Check if we've satisfied this character's requirement
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # Try to shrink window while still valid
            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                
                # Remove leftmost character from window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ("ADOBECODEBANC", "ABC"),  # → "BANC"
        ("a", "a"),                # → "a"
        ("a", "aa"),               # → ""
        ("ab", "b"),               # → "b"
        ("aa", "aa"),              # → "aa"
    ]
    
    for s, t in test_cases:
        print(f"s='{s}', t='{t}'")
        result = sol.minWindow(s, t)
        print(f"Minimum window: '{result}'\n")    