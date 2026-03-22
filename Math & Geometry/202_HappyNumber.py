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