"""
LeetCode 131: Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

Problem Description:
- Given a string s, partition s such that every substring
  of the partition is a palindrome.
- Return all possible palindrome partitioning of s.

Approach:
- Use Depth-First Search (DFS) with backtracking.
- Try every possible prefix starting from index i.
- Only continue recursion if the chosen substring is a palindrome.
- Maintain a list (part) representing the current partition.

Key Observations:
- Each partition must cover the entire string with no gaps.
- Palindrome checking allows pruning of invalid branches early.
- Backtracking ensures exploration of all valid partitions.
- Subproblems overlap in palindrome checks.

Technique: Backtracking (DFS on String)
1. Start DFS from index 0.
2. For each index i, try all substrings s[i:j].
3. If s[i:j] is a palindrome:
   - Add it to the current partition.
   - Recursively process the remaining string starting at j + 1.
4. If the end of the string is reached, record the partition.
5. Backtrack after each recursive call.

Example:
s = "aab"

Valid partitions:
- ["a", "a", "b"]
- ["aa", "b"]

Time Complexity:
- O(n × 2ⁿ)
  - 2ⁿ possible partitions in the worst case
  - Palindrome check costs O(n) per substring

Space Complexity:
- O(n) for recursion depth and current partition
- O(number of valid partitions) for result storage
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # Reached the end of the string
            if i >= len(s):
                res.append(part.copy())
                return

            # Try all possible substrings starting at i
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()  # backtrack

        dfs(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))