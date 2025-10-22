class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        res = [words[0]]
        for i in range(1, len(groups)):
            if groups[i] != groups[i - 1]:
                res.append(words[i])
        return res
