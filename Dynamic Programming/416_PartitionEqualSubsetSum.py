from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for j in dp:
                if target == j + nums[i]:
                    return True
                nextDp.add(j + nums[i])
                nextDp.add(j)
            dp = nextDp

        return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition([1,5,11,5]))  # Expected: True
    print(sol.canPartition([1,2,3,5]))   # Expected: False