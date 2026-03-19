import math

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses digits of a 32-bit signed integer.
        Returns 0 if overflow occurs.
        """

        min_n = -2147483648
        max_n = 2147483647    
        res = 0

        while x:

            # Extract last digit (handles negative correctly)
            digit = int(math.fmod(x, 10))

            # Remove last digit
            x = int(x / 10)

            # Check positive overflow
            if (res > (max_n // 10)) or \
               (res == (max_n // 10) and digit >= max_n % 10):
                return 0
            
            # Check negative overflow
            if (res < (min_n // 10)) or \
               (res == (min_n // 10) and digit <= min_n % 10):
                return 0
            
            # Build reversed number
            res = (res * 10) + digit

        return res

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # overflow case
    ]

    for x, expected in test_cases:
        result = solution.reverse(x)
        status = "✓" if result == expected else "✗"
        print(f"x = {x} → reversed = {result} (Expected: {expected}) {status}")