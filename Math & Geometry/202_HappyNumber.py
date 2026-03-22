"""
LeetCode 202: Happy Number
https://leetcode.com/problems/happy-number/

Approach:
- We are given an integer `n`.
- We repeatedly replace the number with the sum of the squares of its digits.
- The process continues until:
    → We reach 1 → number is HAPPY
    → We enter a cycle → number is NOT happy

Goal:
- Determine whether `n` is a happy number.

Key Observations:
- This process forms a sequence.
- If the number is not happy, it will eventually fall into a cycle.
- To detect cycles, we use a **set** to track visited numbers.

Example:

n = 19

Step-by-step:
19 → 1² + 9² = 82  
82 → 8² + 2² = 68  
68 → 6² + 8² = 100  
100 → 1² + 0² + 0² = 1  

→ Reached 1 → HAPPY

Non-happy example:

n = 2

2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 ...

→ Cycle detected → NOT happy

Technique: HashSet + Cycle Detection

Algorithm:
1. Initialize an empty set `visit`
2. While `n` is not in the set:
   - If `n == 1`, return True
   - Add `n` to the set
   - Replace `n` with sum of squares of its digits
3. If loop ends → cycle detected → return False

Helper Function:
- Extract digits using `% 10`
- Square each digit and accumulate
- Remove digit using `// 10`

Time Complexity:
- Each number eventually falls into a cycle or reaches 1
- The sequence is bounded → effectively O(1)

Space Complexity:
- Set stores visited numbers → O(1) (bounded cycle)
"""

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