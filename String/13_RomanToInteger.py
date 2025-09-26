"""
LeetCode 13: Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Problem:
Given a Roman numeral, convert it to an integer.

Roman numerals are represented by seven symbols: I, V, X, L, C, D, and M.
Symbols can be combined, but certain pairs use subtraction (like IV = 4, IX = 9).

Example:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.

Approach:
- Store the values of Roman symbols in a dictionary.
- Traverse the string:
    - If the current numeral is smaller than the next, subtract it from the next (special case).
    - Otherwise, just add its value.
- Continue until the end and return the total.

Time Complexity: O(n)  
    - Single pass over the input string.
Space Complexity: O(1)  
    - Only a fixed-size dictionary and counters are used.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        n = len(s)
        T_sum = 0

        while i < n:
            if i < n-1 and d[s[i]] < d[s[i+1]]:
                T_sum += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                T_sum += d[s[i]]
                i += 1
        return T_sum
    
    # Example run for local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))  # Expected 1994