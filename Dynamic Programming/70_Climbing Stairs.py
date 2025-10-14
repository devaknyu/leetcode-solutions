class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # Expected output: 2
    print(sol.climbStairs(3))  # Expected output: 3
    print(sol.climbStairs(5))  # Expected output: 8