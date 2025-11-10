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