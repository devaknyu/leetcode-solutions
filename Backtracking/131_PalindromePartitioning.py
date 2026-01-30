
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # Reached the end of the string
            if i >= len(s):
                res.append(part.copy())
                return

            # Try all possible substrings starting at i
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()  # backtrack

        dfs(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))