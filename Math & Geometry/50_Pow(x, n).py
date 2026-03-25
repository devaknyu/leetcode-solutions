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