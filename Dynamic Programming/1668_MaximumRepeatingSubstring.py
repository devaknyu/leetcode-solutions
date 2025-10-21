
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

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxRepeating("ababc", "ab"))   # Expected output: 2
    print(sol.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))  # Expected output: 5
    print(sol.maxRepeating("ab", "ab"))      # Expected output: 1
    print(sol.maxRepeating("a", "aa"))       # Expected output: 0