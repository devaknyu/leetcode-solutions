"""
LeetCode 202: Happy Number
https://leetcode.com/problems/happy-number/

Approach:
- Use a set to track visited numbers.
- Continuously replace n with the sum of the squares of its digits.
- If n becomes 1 → happy number.
- If n repeats (cycle detected) → not a happy number.

Time Complexity: O(log n)
Space Complexity: O(log n)
"""

class solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumofsquare(n)
            if n == 1:
                return True
        return False
    
    def sumofsquare(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output

# Example usage
if __name__ == "__main__":
    sol = solution()
    print(sol.isHappy(19))   # Expected output: True
    print(sol.isHappy(2))    # Expected output: False
