class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))  # Expected output: 2
    print(sol.missingNumber([0, 1]))     # Expected output: 2
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))  # Expected output: 8