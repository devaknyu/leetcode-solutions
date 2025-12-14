class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = m
            else:
                return m
                
        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        4,    # → 2
        8,    # → 2 (sqrt(8) ≈ 2.828, floor is 2)
        0,    # → 0
        1,    # → 1
        16,   # → 4
        25,   # → 5
        26,   # → 5
    ]
    
    for x in test_cases:
        print(f"x = {x}")
        result = sol.mySqrt(x)
        print(f"sqrt(x) = {result} ({result}² = {result*result}, {(result+1)}² = {(result+1)*(result+1)})\n")