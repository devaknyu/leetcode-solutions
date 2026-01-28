"""
LeetCode 22: Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Problem Description:
- Given n pairs of parentheses,
  generate all combinations of well-formed parentheses.
- The answer can be returned in any order.

Approach:
- Use backtracking to build valid parentheses strings step by step.
- Keep track of:
  - openN: number of '(' used so far
  - closedN: number of ')' used so far
- Maintain a stack (list) to construct the current string.

Key Observations:
- We can add '(' as long as openN < n.
- We can add ')' only if closedN < openN
  (to maintain valid parentheses).
- A sequence is valid only when openN == closedN == n.
- Invalid sequences are never explored (early pruning).

Technique: Backtracking (DFS)
1. Start with openN = 0, closedN = 0, and an empty stack.
2. If openN == closedN == n:
   - Join the stack into a string and record it.
3. Recursively explore:
   - Add '(' if openN < n
   - Add ')' if closedN < openN
4. Backtrack after each recursive call.

Example:
n = 3

Valid combinations:
- "((()))"
- "(()())"
- "(())()"
- "()(())"
- "()()()"

Time Complexity:
- O(4ⁿ / √n) (Catalan number growth)
- Only valid sequences are generated due to pruning

Space Complexity:
- O(n) for recursion depth and stack
- O(number of valid combinations) for result storage
"""

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