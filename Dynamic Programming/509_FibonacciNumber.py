class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            a = self.fib(n - 1)
            b = self.fib(n - 2)
            return a + b

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(0))  # Expected output: 0
    print(sol.fib(1))  # Expected output: 1
    print(sol.fib(4))  # Expected output: 3
    print(sol.fib(5))  # Expected output: 5