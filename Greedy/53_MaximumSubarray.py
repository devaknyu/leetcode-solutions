from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSub = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
    print(sol.maxSubArray([1]))                     # Expected: 1
    print(sol.maxSubArray([5,4,-1,7,8]))            # Expected: 23