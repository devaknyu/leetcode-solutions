class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        char = list(s)
        for i in range(0, len(char), 2 * k):
            l = i
            r = min(i + k - 1, len(char) - 1)
            
            while l < r:
                char[l], char[r] = char[r], char[l]
                l += 1
                r -= 1
        return ''.join(char)