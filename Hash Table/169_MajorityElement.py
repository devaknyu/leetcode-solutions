

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))       # Expected output: 3
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Expected output: 2
