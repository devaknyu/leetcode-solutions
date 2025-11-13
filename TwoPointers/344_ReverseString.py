"""
LeetCode 344: Reverse String
https://leetcode.com/problems/reverse-string/

Approach:
- Reverse the string in-place using two pointers
- Swap characters from both ends moving towards the center

Technique: Two-Pointer Swap
1. Left pointer starts at beginning, right pointer at end
2. Swap characters at both pointers
3. Move pointers inward until they meet

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(s) - 1

        while R > L:
            # Swap characters at L and R positions
            tmp = s[L]
            s[L] = s[R]
            s[R] = tmp
            L += 1
            R -= 1
        return s

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        (["h","e","l","l","o"]),      # → ["o","l","l","e","h"]
        (["H","a","n","n","a","h"]),  # → ["h","a","n","n","a","H"]
        (["a","b"]),                  # → ["b","a"]
        (["a"]),                      # → ["a"]
        ([],)                         # → []
    ]
    
    for input_chars in test_cases:
        test_input = list(input_chars)  # Convert tuple to list
        print(f"Input:  {test_input}")
        sol.reverseString(test_input)
        print(f"Output: {test_input}\n")