class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Returns True if n is a happy number, else False.
        """

        visit = set()

        while n not in visit:

            if n == 1:
                return True

            visit.add(n)

            n = self.sumofsquares(n)

        return False
    
    def sumofsquares(self, n: int) -> int:
        """
        Returns sum of squares of digits of n.
        """

        output = 0

        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10

        return output

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (19, True),
        (2, False),
        (1, True),
        (7, True),
    ]

    for n, expected in test_cases:
        result = solution.isHappy(n)
        status = "✓" if result == expected else "✗"
        print(f"n = {n} → isHappy = {result} (Expected: {expected}) {status}")