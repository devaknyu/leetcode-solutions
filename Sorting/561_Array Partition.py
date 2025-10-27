class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        result = 0

        for i in range(0, len(sorted_nums), 2):
            result += sorted_nums[i]
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayPairSum([1, 4, 3, 2]))     # Expected output: 4
    print(sol.arrayPairSum([6, 2, 6, 5, 1, 2]))  # Expected output: 9
    print(sol.arrayPairSum([1, 1, 1, 1]))     # Expected output: 2