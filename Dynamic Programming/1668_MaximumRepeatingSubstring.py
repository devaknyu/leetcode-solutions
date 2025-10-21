
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_rep = 0
        i = 0
        while i < len(sequence):
            rep = 0
            while sequence[i : i + len(word)] == word:
                rep += 1
                i += len(word)
            if rep:
                max_rep = max(max_rep, rep)
                i -= len(word)
            i += 1
        return max_rep