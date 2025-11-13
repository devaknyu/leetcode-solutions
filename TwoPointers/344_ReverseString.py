from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(s) - 1

        while R > L:
            # Swap characters at L and R positions
            tmp = s[L]
            s[L] = s[R]
            s[R] = tmp
            L += 1
            R -= 1
        return s