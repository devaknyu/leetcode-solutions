"""
LeetCode 150: Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Approach:
- Evaluate arithmetic expression in Reverse Polish Notation (postfix notation)
- Use stack to store operands and perform operations
- When operator encountered, pop two operands, apply operation, push result

Technique: Stack-based Evaluation
1. Traverse tokens from left to right
2. If operand (number), push to stack
3. If operator, pop two operands, apply operation, push result
4. For division, ensure integer division truncates toward zero
5. Note order: second popped operand is first in expression

Time Complexity: O(n) - single pass through tokens
Space Complexity: O(n) - stack stores operands
"""

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # Truncate toward zero
            else:
                stack.append(int(token))
        return stack[0]


# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ["2", "1", "+", "3", "*"],  # → 9 ( (2+1)*3 )
        ["4", "13", "5", "/", "+"], # → 6 ( 4 + (13/5) )
        ["10", "6", "9", "3", "/", "-11", "*", "+", "*", "17", "+", "5", "+"],  # → 22
        ["4", "3", "-"],  # → 1
        ["3", "4", "+"],  # → 7
    ]
    
    for tokens in test_cases:
        print(f"Tokens: {tokens}")
        result = sol.evalRPN(tokens)
        print(f"Result: {result}\n")
