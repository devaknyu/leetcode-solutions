"""
LeetCode 2900: Longest Unequal Adjacent Groups Subsequence I
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

Approach:
- We are given two lists:
  1. `words` — a list of strings.
  2. `groups` — a list of integers where each number represents the group ID of the corresponding word.
- The goal is to construct the **longest subsequence** of words such that **no two adjacent words** in the subsequence belong to the **same group**.

Steps:
1. Start with the first word in the result (`res = [words[0]]`).
2. Iterate through the remaining words:
   - For each index `i`, if `groups[i] != groups[i-1]`, 
     it means the group changes, so append `words[i]` to `res`.
3. Return the final list `res`.

Example:
Input:
  words = ["a", "b", "c", "d"]
  groups = [1, 2, 2, 1]
Output:
  ["a", "b", "d"]
Explanation:
- "a" (group 1) → "b" (group 2) are from different groups.
- Skip "c" (same group as "b").
- "d" (group 1) is different from the previous (group 2), so include it.

Time Complexity: O(n)
Space Complexity: O(n)
"""

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