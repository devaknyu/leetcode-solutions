from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN, closedN):
            # Valid complete sequence
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # Add '(' if we still can
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            # Add ')' only if it keeps the sequence valid
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))