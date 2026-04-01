"""
LeetCode 271: Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/

Approach:
- Encode: For each string, store length + delimiter + string content
- Decode: Parse length, skip delimiter, extract string of that length

Technique: Length-Prefixed Encoding
1. Encode: Convert list to string with format "length#string"
2. Decode: Find length before '#', then read exactly that many characters
3. Handles empty strings and special characters including '#'

Time Complexity: O(n) for both encode and decode
Space Complexity: O(n) for encoded string
"""

from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res


# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ["hello", "world"],
        ["", ""],
        ["a", "b", "c"],
        ["#", "##", "###"],
        [],
    ]
    
    for strs in test_cases:
        encoded = sol.encode(strs)
        decoded = sol.decode(encoded)
        print(f"Input:  {strs}")
        print(f"Encoded: '{encoded}'")
        print(f"Decoded: {decoded}")
        print(f"Match: {strs == decoded}\n")
