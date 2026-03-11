"""
LeetCode 678: Valid Parenthesis String
https://leetcode.com/problems/valid-parenthesis-string/

Problem Description:
- You are given a string `s` containing three possible characters:
    '('  → open parenthesis
    ')'  → close parenthesis
    '*'  → wildcard

- The wildcard '*' can represent:
      '('  OR  ')'  OR  an empty string ""

Goal:
- Determine if the string can be interpreted as a **valid
  parentheses string**.

A valid parentheses string means:
1) Every '(' has a matching ')'
2) Parentheses are closed in the correct order.

Examples:
s = "()"
→ True

s = "(*)"
→ True
Explanation:
'*' can act as empty → "()"

s = "(*))"
→ True
Explanation:
'*' can act as '(' → "(())"

s = "(((*)"
→ False

Approach (Greedy Range Tracking):

Key Idea:
- Because '*' can act as multiple possibilities, we track
  a **range of possible open parentheses counts**.

We maintain:
    leftMin → minimum possible open '('
    leftMax → maximum possible open '('

This range represents all possible valid states while
processing the string.

Step-by-step logic:

1) Initialize:
      leftMin = 0
      leftMax = 0

2) Traverse each character `c` in the string.

3) If c == "(":
      leftMin += 1
      leftMax += 1

   We definitely added an open parenthesis.

4) If c == ")":
      leftMin -= 1
      leftMax -= 1

   We close a parenthesis.

5) If c == "*":
   '*' could be:
      '('  → increase open
      ')'  → decrease open
      ""   → do nothing

   So:
      leftMax += 1   (treat as '(')
      leftMin -= 1   (treat as ')')

6) If leftMax < 0:
      Too many ')' → impossible → return False.

7) If leftMin < 0:
      Clamp it to zero:
      leftMin = 0

   Because minimum open parentheses cannot go negative.

8) After processing the whole string:
      return leftMin == 0

   Meaning we can balance all parentheses.

Example:
s = "(*))"

Step-by-step:

start:
leftMin = 0
leftMax = 0

'('
leftMin = 1
leftMax = 1

'*'
leftMin = 0
leftMax = 2

')'
leftMin = -1 → clamp → 0
leftMax = 1

')'
leftMin = -1 → clamp → 0
leftMax = 0

Final:
leftMin == 0 → valid.

Time Complexity: O(n)
- Single pass through the string.

Space Complexity: O(1)
- Only two integer variables are used.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax, leftMin = 0, 0

        for c in s:
            if c == "(":
                leftMax += 1
                leftMin += 1

            elif c == ")":
                leftMax -= 1
                leftMin -= 1

            else:  # '*'
                leftMax += 1
                leftMin -= 1

            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0

        return leftMin == 0

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkValidString("()"))    # Expected: True
    print(sol.checkValidString("(*)"))   # Expected: True
    print(sol.checkValidString("(*))"))  # Expected: True
    print(sol.checkValidString("(((*)")) # Expected: False