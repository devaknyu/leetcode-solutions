class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Computes x raised to the power n.
        """

        def helper(x, n):

            if x == 0:
                return 0

            if n == 0:
                return 1

            # Divide step
            res = helper(x, n // 2)

            # Conquer step (square)
            res = res * res

            # If n is odd, multiply one extra x
            return x * res if n % 2 else res

        # Handle negative exponent
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
    
# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (0.0, 5, 0.0),
    ]

    for x, n, expected in test_cases:
        result = solution.myPow(x, n)
        status = "✓" if abs(result - expected) < 1e-5 else "✗"
        print(f"x = {x}, n = {n} → result = {result} (Expected: {expected}) {status}")