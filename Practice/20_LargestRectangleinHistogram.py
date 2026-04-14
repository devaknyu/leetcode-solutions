"""
LeetCode 84: Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Approach:
- Find maximum area rectangle formed by histogram bars
- Use monotonic increasing stack to track bar indices and heights
- When smaller bar encountered, calculate areas for previous taller bars
- Process remaining bars at the end

Technique: Monotonic Stack
1. Stack stores [starting_index, height] pairs
2. Maintain stack in increasing height order
3. When smaller height encountered, pop taller bars and calculate their areas
4. Update starting index for current bar based on popped bars
5. Process remaining bars after main loop

Time Complexity: O(n) - each bar pushed and popped once
Space Complexity: O(n) - stack storage
"""

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # stores [starting_index, height]

        for i, h in enumerate(heights):
            start = i
            # While current height is smaller than stack top
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area for popped bar
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append([start, h])

        # Process remaining bars in stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [2, 1, 5, 6, 2, 3],  # → 10
        [2, 4],              # → 4
        [1],                 # → 1
        [2, 1, 2],           # → 3
    ]
    
    for heights in test_cases:
        print(f"Histogram: {heights}")
        result = sol.largestRectangleArea(heights)
        print(f"Largest rectangle area: {result}\n")
