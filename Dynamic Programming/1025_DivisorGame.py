class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.divisorGame(2))  # Expected output: True
    print(sol.divisorGame(3))  # Expected output: False
    print(sol.divisorGame(10)) # Expected output: True