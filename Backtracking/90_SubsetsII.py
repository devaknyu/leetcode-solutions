from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset):
            # Reached the end → record subset
            if i == len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)

            # Backtrack
            subset.pop()

            # Skip all duplicates of nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i] and move forward
            dfs(i + 1, subset)

        dfs(0, [])
        return res

if __name__ == "__main__":
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))