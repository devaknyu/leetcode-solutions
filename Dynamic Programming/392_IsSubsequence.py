class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == len(s) else False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))  # Expected output: True
    print(sol.isSubsequence("axc", "ahbgdc"))  # Expected output: False
    print(sol.isSubsequence("", "ahbgdc"))     # Expected output: True (empty string is always a subsequence)