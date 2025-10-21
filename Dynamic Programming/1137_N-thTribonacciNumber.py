
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]

        if n < 3:
            return t[n]

        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
        return t[2]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci(4))   # Expected output: 4
    print(sol.tribonacci(25))  # Expected output: 1389537
    print(sol.tribonacci(0))   # Expected output: 0