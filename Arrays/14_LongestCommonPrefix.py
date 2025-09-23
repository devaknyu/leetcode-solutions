"""
LeetCode 14: Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Approach:
- Start with an empty result string.
- Iterate through each character index of the first string.
- For each index, check if all other strings have the same character at that position.
- If a mismatch or string end is found, return the current result.
- Otherwise, append the character to the result.

Time Complexity: O(N * M), where:
    N = number of strings
    M = length of the shortest string
Space Complexity: O(1)   (only storing the prefix string)
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
    # Example run for local testing
if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))      # Output: ""
