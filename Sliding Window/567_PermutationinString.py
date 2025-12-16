"""
LeetCode 567: Permutation in String
https://leetcode.com/problems/permutation-in-string/

Approach:
- Check if s2 contains a permutation (anagram) of s1
- Use sliding window with character frequency counting
- Compare frequency arrays of s1 and current window in s2
- Use matches counter to track how many characters have matching frequencies

Technique: Sliding Window with Frequency Arrays
1. Create frequency arrays for s1 and first window of s2
2. Count matches (positions where frequencies are equal)
3. Slide window through s2, updating frequencies and matches
4. Return True if matches == 26 (all characters match)

Time Complexity: O(n) where n is length of s2
Space Complexity: O(1) - fixed size arrays of 26
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1count = [0] * 26
        s2count = [0] * 26
        
        # Initialize frequency arrays for first window
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        # Count initial matches
        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0
        
        # Slide window through s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add new character on right
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            # Remove old character on left
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        
        return matches == 26
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ("ab", "eidbaooo"),   # → True
        ("ab", "eidboaoo"),   # → False
        ("a", "ab"),          # → True
        ("abc", "bbbca"),     # → True
        ("hello", "ooolleoooleh"),  # → False
    ]
    
    for s1, s2 in test_cases:
        print(f"s1='{s1}', s2='{s2}'")
        result = sol.checkInclusion(s1, s2)
        print(f"Permutation found: {result}\n")