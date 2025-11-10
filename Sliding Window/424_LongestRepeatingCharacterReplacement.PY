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