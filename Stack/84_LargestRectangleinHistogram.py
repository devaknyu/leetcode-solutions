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