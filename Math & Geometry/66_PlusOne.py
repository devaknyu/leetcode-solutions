"""
LeetCode 66: Plus One
https://leetcode.com/problems/plus-one/

Approach:
- We are given a large integer represented as an array of digits.
- Each element contains a single digit.
- The goal is to add 1 to the number and return the resulting array.

Key Observations:
- Addition starts from the least significant digit (rightmost).
- If a digit is 9:
    → It becomes 0 (carry over)
- Otherwise:
    → Simply increment the digit and stop

Example:

digits = [1,2,3]
→ [1,2,4]

digits = [1,2,9]
→ [1,3,0]

digits = [9,9,9]
→ [1,0,0,0]

Key Idea:
- Reverse the array to process from least significant digit easily.
- Keep a `carry` (called `one` in your code).
- Continue until carry is resolved.

Technique: Simulation (Digit-wise Addition)

Algorithm:
1. Reverse the digits array
2. Initialize carry = 1 (since we are adding one)
3. Iterate through digits:
   - If digit is 9 → set to 0 (carry continues)
   - Else → increment digit and stop carry
4. If carry still exists after loop → append 1
5. Reverse the array back and return

Time Complexity:
- O(n)

Space Complexity:
- O(1) extra (ignoring output)
"""


class Solution:
    def plusOne(self, digits):
        """
        Adds one to the number represented by digits.
        """

        # Reverse to process from least significant digit
        digits = digits[::-1]

        one, i = 1, 0

        while one:

            if i < len(digits):

                if digits[i] == 9:
                    digits[i] = 0  # carry continues
                else:
                    digits[i] += 1
                    one = 0  # carry resolved

            else:
                # All digits were 9 (e.g., 999 → 1000)
                digits.append(1)
                one = 0

            i += 1

        return digits[::-1]

# Example usage
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
        ([9,9,9], [1,0,0,0]),
    ]

    for digits, expected in test_cases:
        result = solution.plusOne(digits[:])  # copy to preserve original
        status = "✓" if result == expected else "✗"
        print(f"digits = {digits} → result = {result} (Expected: {expected}) {status}")