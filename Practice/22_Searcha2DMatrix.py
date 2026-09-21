"""
LeetCode 74: Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

Approach:
- Search for target in m x n matrix where:
  1. Each row is sorted left to right
  2. First element of each row > last element of previous row
- Use binary search to find correct row, then binary search within row

Technique: Two-Step Binary Search
1. Binary search to find correct row by comparing target with first/last element
2. Binary search within selected row to find target

Time Complexity: O(log m + log n) = O(log(m*n))
Space Complexity: O(1) - only constant extra space
"""

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1
        
        # Binary search to find correct row
        while top <= bot:
            mid_r = (bot + top) // 2
            if target > matrix[mid_r][-1]:
                top = mid_r + 1
            elif target < matrix[mid_r][0]:
                bot = mid_r - 1
            else:
                break
        
        # If no valid row found
        if not (top <= bot):
            return False
        
        mid_r = (bot + top) // 2
        
        # Binary search within the row
        l, r = 0, COL - 1
        while l <= r:
            mid_c = (r + l) // 2
            if target > matrix[mid_r][mid_c]:
                l = mid_c + 1
            elif target < matrix[mid_r][mid_c]:
                r = mid_c - 1
            else:
                return True
                
        return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),   # → True
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),  # → False
        ([[1]], 1),                                                # → True
        ([[1, 3]], 3),                                             # → True
    ]
    
    for matrix, target in test_cases:
        print(f"Matrix: {matrix}")
        print(f"Target: {target}")
        result = sol.searchMatrix(matrix, target)
        print(f"Found: {result}\n")