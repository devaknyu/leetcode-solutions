class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
            
        l, r = 0, num
        
        while l <= r:
            m = (r + l) // 2
            square = m * m
            
            if square == num:
                return True
            elif square > num:
                r = m - 1
            else:
                l = m + 1
        
        return False
