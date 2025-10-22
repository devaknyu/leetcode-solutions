class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        res = [words[0]]
        for i in range(1, len(groups)):
            if groups[i] != groups[i - 1]:
                res.append(words[i])
        return res
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.getLongestSubsequence(["a", "b", "c", "d"], [1, 2, 2, 1]))  # Expected output: ["a", "b", "d"]
    print(sol.getLongestSubsequence(["hello", "world"], [0, 1]))          # Expected output: ["hello", "world"]
    print(sol.getLongestSubsequence(["x", "y", "z"], [1, 1, 1]))          # Expected output: ["x"]