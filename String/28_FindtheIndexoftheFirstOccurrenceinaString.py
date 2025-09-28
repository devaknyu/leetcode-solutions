"""
LeetCode 28: Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Problem:
Given two strings `haystack` and `needle`, return the index of the first occurrence
of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Approach:
- If needle is empty, return 0 (per problem statement).
- Use a sliding window approach:
    - Iterate `i` over possible starting indices in `haystack` 
      where `needle` could fit (`0` → `len(haystack) - len(needle)`).
    - For each window, compare character by character.
    - If all characters match, return the index `i`.
- If no match found, return -1.

Time Complexity: O((n - m + 1) * m)  
    - n = len(haystack), m = len(needle).
    - In worst case, compare m characters at each of (n-m+1) positions.
Space Complexity: O(1)  
    - No extra data structures used.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
    
    # Example run for local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))   # Expected 0
    print(sol.strStr("leetcode", "leeto"))  # Expected -1