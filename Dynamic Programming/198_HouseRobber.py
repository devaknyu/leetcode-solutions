from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            tmp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = tmp

        return rob2

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))      # Expected output: 4
    print(sol.rob([2, 7, 9, 3, 1]))   # Expected output: 12