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