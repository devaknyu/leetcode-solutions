"""
LeetCode 139: Word Break
https://leetcode.com/problems/word-break/

Problem Description:
- Given a string `s` and a list of strings `wordDict`,
  return True if `s` can be segmented into a space-separated
  sequence of one or more dictionary words.
- Words in the dictionary may be reused multiple times.

Examples:
s = "leetcode", wordDict = ["leet", "code"] → True
Explanation: "leet code"

s = "applepenapple", wordDict = ["apple", "pen"] → True
Explanation: "apple pen apple"

s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"] → False

Approach (Bottom-Up Dynamic Programming):

Key Idea:
- Let dp[i] represent whether substring s[i:] can be segmented
  using words from wordDict.
- We compute from right to left.

Initialization:
- dp = [False] * (len(s) + 1)
- dp[len(s)] = True
  (Empty string can always be segmented.)

Transition:
For each index i from len(s)-1 down to 0:
    For each word w in wordDict:
        If:
            1) s[i:i+len(w)] == w
            2) dp[i + len(w)] is True
        Then:
            dp[i] = True
            break early (no need to check other words)

Final Answer:
- Return dp[0]
  (Can the entire string be segmented?)

Example:
s = "leetcode"
wordDict = ["leet", "code"]

dp initially:
[False, False, False, False, False, False, False, False, True]

Working backward:
i = 4 → "code" matches and dp[8] is True → dp[4] = True
i = 0 → "leet" matches and dp[4] is True → dp[0] = True

Return True

Time Complexity: O(n * m * k)
- n = length of s
- m = number of words
- k = average word length
(We compare substrings for each word at each index.)

Space Complexity: O(n)
- DP array of size n+1.
"""

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"]))  # Expected: True
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Expected: Fal