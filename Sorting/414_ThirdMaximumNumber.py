class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        sorted_nums = sorted(unique_nums, reverse=True)

        if len(sorted_nums) > 2:
            return sorted_nums[2]
        else:
            return sorted_nums[0]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.thirdMax([3, 2, 1]))         # Expected output: 1
    print(sol.thirdMax([1, 2]))            # Expected output: 2
    print(sol.thirdMax([2, 2, 3, 1]))      # Expected output: 1
    print(sol.thirdMax([5, 7, 7, 7, 8]))   # Expected output: 8
