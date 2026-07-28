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
