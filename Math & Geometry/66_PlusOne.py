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
