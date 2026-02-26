from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LEN = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LEN[i] = max(LEN[i], LEN[j] + 1)

        return max(LEN)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Expected: 4
    print(sol.lengthOfLIS([0,1,0,3,2,3]))         # Expected: 4
    print(sol.lengthOfLIS([7,7,7,7,7]))           # Expected: 1