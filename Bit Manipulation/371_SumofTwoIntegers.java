/*
LeetCode 371: Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/

Approach:
- We are given two integers `a` and `b`.
- The goal is to compute their sum WITHOUT using '+' or '-' operators.

Key Observations:
- Binary addition consists of two parts:
  1. Sum without carry
  2. Carry

We can simulate this using bit operations:

1. XOR (a ^ b) → gives the sum WITHOUT carry
2. AND (a & b) → gives the carry bits (before shifting)
3. Left shift ((a & b) << 1) → moves carry to correct position

Core Idea:
- Repeat the process until there is no carry left.

Example:
a = 5  (0101)
b = 3  (0011)

Step 1:
sum = a ^ b = 0110 (6)
carry = (a & b) << 1 = (0001) << 1 = 0010 (2)

Step 2:
a = 6, b = 2

sum = 0110 ^ 0010 = 0100 (4)
carry = (0110 & 0010) << 1 = (0010) << 1 = 0100 (4)

Step 3:
a = 4, b = 4

sum = 0100 ^ 0100 = 0000 (0)
carry = (0100 & 0100) << 1 = (0100) << 1 = 1000 (8)

Step 4:
a = 0, b = 8

sum = 0000 ^ 1000 = 1000 (8)
carry = 0 → STOP

Result = 8

Technique: Bit Manipulation (Binary Addition Simulation)

Algorithm:
1. While `b` (carry) is not zero:
   - Compute carry: (a & b) << 1
   - Compute sum without carry: a ^ b
   - Update `a` to sum
   - Update `b` to carry
2. Return `a`

Why it works:
- XOR adds bits ignoring carry
- AND identifies where carry occurs
- Shifting moves carry to the next higher bit
- Repeating resolves cascading carries

Time Complexity:
- O(1) → at most 32 iterations for 32-bit integers

Space Complexity:
- O(1)
*/


class Solution {
    public int getSum(int a, int b) {

        while (b != 0) {

            // Carry calculation
            int tmp = (a & b) << 1;

            // Sum without carry
            a = a ^ b;

            // Update carry
            b = tmp;
        }

        return a;
    }
}

// Example usage
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] testCases = {
            {1, 2, 3},
            {2, 3, 5},
            {-2, 3, 1},
            {-5, -7, -12},
            {0, 0, 0}
        };

        for (int[] test : testCases) {
            int a = test[0];
            int b = test[1];
            int expected = test[2];

            int result = solution.getSum(a, b);
            String status = (result == expected) ? "✓" : "✗";

            System.out.println(
                "a = " + a + ", b = " + b +
                " → sum = " + result +
                " (Expected: " + expected + ") " + status
            );
        }
    }
}