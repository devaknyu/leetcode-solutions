import collections
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        max_length = 0

        for num in count:
            if num + 1 in count:
                length = count[num] + count[num + 1]
                if length > max_length:
                    max_length = length
        return max_length

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # Expected output: 5
    print(sol.findLHS([1, 1, 1, 1]))              # Expected output: 0
    print(sol.findLHS([1, 2, 3, 4]))              # Expected output: 2