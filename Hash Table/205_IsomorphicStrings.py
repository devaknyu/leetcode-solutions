"""
LeetCode 205: Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Approach:
- Use two hash maps to maintain mappings between s → t and t → s.
- Iterate over both strings simultaneously.
- If a mapping conflict occurs (e.g., same character maps to different targets), return False.
- Otherwise, continue and return True if all mappings are consistent.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True
    

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))     # Expected output: True
    print(sol.isIsomorphic("foo", "bar"))     # Expected output: False
    print(sol.isIsomorphic("paper", "title")) # Expected output: True
    print(sol.isIsomorphic("ab", "aa"))       # Expected output: False