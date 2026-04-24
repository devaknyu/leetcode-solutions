"""
LeetCode 424: Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Approach:
- We need to find the length of the longest substring containing the same letter 
  that can be obtained by changing at most k characters.
- This is a sliding window problem where we maintain a valid window that can be 
  converted to all same characters with at most k replacements.

Technique: Sliding Window with HashMap (Dictionary)
1. Use two pointers (l and r) to represent the current window boundaries.
2. Maintain a frequency count of characters in the current window using a dictionary.
3. The key insight: A window is valid if (window_length - max_frequency) <= k
   - window_length = r - l + 1
   - max_frequency = highest frequency of any character in current window
   - The difference represents how many characters need to be replaced
4. Expand the window by moving r pointer:
   - Update frequency count for the new character
   - If the window becomes invalid (needs more than k replacements), shrink from left
5. Track the maximum valid window length encountered.

Why this works:
- The window always tries to stay as large as possible while remaining valid
- We only shrink when necessary (i.e., when replacements exceed k)
- Using a dictionary allows handling any character set dynamically

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

Time Complexity: O(n * 26) ≈ O(n)
- Each step computes max(count.values()), which is bounded by character set size

Space Complexity: O(1)
- At most 26 keys (uppercase English letters) in dictionary
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0

        for r in range(len(s)):
            # Add current character to frequency count
            count[s[r]] = 1 + count.get(s[r], 0)

            # Shrink window if it needs more than k replacements
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # Update longest valid window
            res = max(res, r - l + 1)

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("AAAB", 0, 3),
        ("ABBB", 2, 4),
        ("", 1, 0),
        ("A", 0, 1),
    ]

    for s, k, expected in test_cases:
        result = sol.characterReplacement(s, k)
        status = "✓" if result == expected else "✗"
        print(f"'{s}', k={k} → {result} (Expected: {expected}) {status}")