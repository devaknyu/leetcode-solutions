"""
Approach:
- The game starts with a number `n`.
- Two players (Alice and Bob) take turns choosing a number `x` such that:
  1 <= x < n and n % x == 0  
  Then, `n` becomes `n - x`.
- The player who cannot make a move loses.
- Alice always starts first.

Mathematical Insight:
- If `n` is even → Alice **always wins**.
  - Alice can always choose `x = 1`, making `n` odd for Bob.
  - From then on, every move alternates between even and odd.
  - Eventually, Bob gets `n = 1` (no moves left) and loses.
- If `n` is odd → Alice **always loses**.
  - Any divisor `x` of an odd number is odd.
  - Subtracting an odd number keeps the result even → Bob gets an even number and wins.

Thus, the result depends solely on whether `n` is even.

Example:
n = 2 → True (Alice wins)
n = 3 → False (Bob wins)

Time Complexity: O(1)
Space Complexity: O(1)
"""

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