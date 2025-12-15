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
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        16,    # → True (4²)
        14,    # → False
        1,     # → True (1²)
        9,     # → True (3²)
        25,    # → True (5²)
        26,    # → False
        100,   # → True (10²)
    ]
    
    for num in test_cases:
        print(f"num = {num}")
        result = sol.isPerfectSquare(num)
        print(f"Perfect square: {result}\n")