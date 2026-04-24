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