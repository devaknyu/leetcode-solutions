"""
LeetCode 20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example:
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Approach:
- Use a stack to keep track of opening brackets.
- Maintain a mapping of closing → opening brackets.
- For each character:
    - If it's a closing bracket, check if the top of the stack matches the corresponding opening.
    - If mismatch, return False immediately.
    - Otherwise, push opening brackets to stack.
- At the end, the stack must be empty for the string to be valid.

Time Complexity: O(n)  
    - We process each character once.
Space Complexity: O(n)  
    - Stack can hold up to n characters in the worst case.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack

# Example run for local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))  # Expected True
    print(sol.isValid("(]"))      # Expected False