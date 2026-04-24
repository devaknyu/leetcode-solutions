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