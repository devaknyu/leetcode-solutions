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