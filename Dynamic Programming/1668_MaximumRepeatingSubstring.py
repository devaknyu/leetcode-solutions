"""
LeetCode 1668: Maximum Repeating Substring
https://leetcode.com/problems/maximum-repeating-substring/

Approach:
- We need to find the maximum number of times `word` can repeat consecutively in `sequence`.
- Iterate through each character index `i` in `sequence`:
  - At each index, check if `word` repeats consecutively starting at `i`.
  - Use a nested loop to repeatedly match substrings of length `len(word)`.
  - Count how many times `word` repeats in a row (`rep`).
  - Update `max_rep` with the maximum value of `rep` seen so far.
  - If a match occurred, move `i` back by one `word` length to avoid skipping possible overlaps.
- Continue until all possible positions are checked.

Example:
sequence = "ababc", word = "ab" → Output: 2  
Explanation: "ab" repeats twice starting at index 0.

Time Complexity: O(n * m), where n = len(sequence) and m = len(word)
Space Complexity: O(1)
"""
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