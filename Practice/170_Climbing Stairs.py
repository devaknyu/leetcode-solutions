class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [1, 2, 3, 4, 5]

    for n in test_cases:
        result = sol.climbStairs(n)
        print(f"n={n} → {result}")