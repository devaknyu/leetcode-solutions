class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPal(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        res = 0
        for i in range(len(s)):
            res += countPal(s, i, i)      # Odd-length
            res += countPal(s, i, i + 1)  # Even-length

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))  # Expected: 3
    print(sol.countSubstrings("aaa"))  # Expected: 6
