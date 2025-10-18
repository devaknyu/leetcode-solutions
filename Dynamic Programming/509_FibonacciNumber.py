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
