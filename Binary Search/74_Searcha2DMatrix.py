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