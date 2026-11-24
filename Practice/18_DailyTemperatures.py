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

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [73, 74, 75, 71, 69, 72, 76, 73],  # → [1,1,4,2,1,1,0,0]
        [30, 40, 50, 60],                   # → [1,1,1,0]
        [30, 60, 90],                       # → [1,1,0]
        [55, 54, 53, 52],                   # → [0,0,0,0]
    ]
    
    for temperatures in test_cases:
        print(f"Temperatures: {temperatures}")
        result = sol.dailyTemperatures(temperatures)
        print(f"Result:       {result}\n")