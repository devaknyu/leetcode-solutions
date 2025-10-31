class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
        return nums

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0, 1, 0, 3, 12]))  # Expected output: [1, 3, 12, 0, 0]
    print(sol.moveZeroes([0, 0, 1]))         # Expected output: [1, 0, 0]
    print(sol.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))  # Expected output: [4,2,4,3,5,1,0,0,0,0]