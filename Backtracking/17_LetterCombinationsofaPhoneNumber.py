"""
LeetCode 17: Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Problem Description:
- Given a string containing digits from 2–9 inclusive,
  return all possible letter combinations that the number could represent.
- The mapping of digits to letters follows the telephone keypad.
- Return the answer in any order.

Approach:
- Use backtracking to build combinations character by character.
- At each digit index, iterate over all possible letters mapped to that digit.
- Append one letter and move to the next digit.

Key Observations:
- Each digit represents a set of choices (branching factor).
- The length of every valid combination equals the length of digits.
- An empty input should return an empty list.
- No pruning is needed beyond reaching the target length.

Technique: Backtracking (DFS on Choices)
1. If the input string is empty, return an empty list.
2. Start backtracking from index 0 with an empty string.
3. For the current digit, iterate over all mapped letters.
4. Append a letter, recurse to the next index, then backtrack.
5. When the current string length equals digits length, record it.

Example:
digits = "23"

Output:
["ad","ae","af","bd","be","bf","cd","ce","cf"]

Time Complexity:
- O(4ⁿ), where n is the length of digits
  (each digit has at most 4 possible letters)

Space Complexity:
- O(n) for recursion depth
- O(4ⁿ) for result storage
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            # Completed one valid combination
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # Explore all letters for current digit
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))