from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: one empty permutation
        if len(nums) == 0:
            return [[]]

        # Get permutations of remaining elements
        perms = self.permute(nums[1:])
        res = []

        # Insert nums[0] into every position of each permutation
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
