"""
LeetCode 739: Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Approach:
- For each day, find number of days until a warmer temperature
- Use monotonic decreasing stack to track temperatures and indices
- When warmer temperature found, calculate days difference and update result

Technique: Monotonic Stack
1. Stack stores [temperature, index] pairs
2. Maintain stack in decreasing temperature order
3. When current temperature > stack top, we found warmer day
4. Calculate days difference = current index - stack index
5. Repeat until stack empty or current temperature <= stack top

Time Complexity: O(n) - each temperature pushed and popped once
Space Complexity: O(n) - stack storage
"""

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores [temperature, index]
        
        for i, t in enumerate(temperatures):
            # While current temperature is warmer than stack top
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append([t, i])
            
        return res