"""
LeetCode 424: Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Approach:
- We need to find the length of the longest substring containing the same letter 
  that can be obtained by changing at most k characters.
- This is a sliding window problem where we maintain a valid window that can be 
  converted to all same characters with at most k replacements.

Technique: Sliding Window with Frequency Count
1. Use two pointers (L and R) to represent the current window boundaries.
2. Maintain a frequency count of characters in the current window.
3. The key insight: A window is valid if (window_length - max_frequency) <= k
   - window_length = R - L + 1
   - max_frequency = count of most frequent character in current window
   - The difference represents how many characters need to be replaced
4. Expand the window by moving R pointer:
   - Update frequency count for the new character
   - If the window becomes invalid (needs more than k replacements), shrink from left
5. Track the maximum valid window length encountered.

Why this works:
- We don't need to shrink the window more than necessary because we're looking for the maximum length
- The condition (window_length - max_frequency) <= k ensures we can convert the window 
  to all same characters with at most k changes

Example:
Input: s = "ABAB", k = 2
Process:
  Window: "A" → "AB" → "ABA" → "ABAB" 
  For "ABAB": length=4, max_freq=2 (A or B), 4-2=2 <= k=2 ✓
Output: 4

Input: s = "AABABBA", k = 1
Process:
  Longest valid window: "AABAB" → convert B to A → "AAAAB"
Output: 4

Time Complexity: O(n) — each character processed once (R pointer) and removed once (L pointer)
Space Complexity: O(1) — fixed size frequency array of 26 elements
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        longest = 0 
        count = [0] * 26  # Frequency count for A-Z

        for R in range(len(s)):
            # Add current character to frequency count
            count[ord(s[R]) - 65] += 1
            
            # Shrink window if it needs more than k replacements
            while (R - L + 1) - max(count) > k:
                count[ord(s[L]) - 65] -= 1
                L += 1
            
            # Update longest valid window
            window_size = R - L + 1
            longest = max(longest, window_size)

        return longest

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ("ABAB", 2, 4),        # Change 2 B's to A's or vice versa
        ("AABABBA", 1, 4),     # Change middle B to A: "AABABBA" → "AAAABBA"
        ("AAAA", 2, 4),        # No changes needed
        ("AAAB", 0, 3),        # Can't change any characters
        ("ABBB", 2, 4),        # Change A to B
        ("", 1, 0),            # Empty string
        ("A", 0, 1),           # Single character
    ]

    
    for s, k, expected in test_cases:
        result = sol.characterReplacement(s, k)
        status = "✓" if result == expected else "✗"
        print(f"'{s}', k={k} → {result} (Expected: {expected}) {status}")