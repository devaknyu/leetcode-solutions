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