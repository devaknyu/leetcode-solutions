class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_S, sum_T = 0, 0
        for i in s:
            sum_S += ord(i)
        for i in t:
            sum_T += ord(i)
        return chr(sum_T - sum_S)