from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))  # Expected: True
    print(sol.canJump([3,2,1,0,4]))  # Expected: False
    print(sol.canJump([2,0]))        # Expected: True