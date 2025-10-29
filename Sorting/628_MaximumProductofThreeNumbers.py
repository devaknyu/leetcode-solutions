from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        product = max(
            sorted_nums[0] * sorted_nums[1] * sorted_nums[2],
            sorted_nums[0] * sorted_nums[-1] * sorted_nums[-2]
        )
        return product
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumProduct([1, 2, 3]))            # Expected output: 6
    print(sol.maximumProduct([1, 2, 3, 4]))         # Expected output: 24
    print(sol.maximumProduct([-10, -10, 5, 2]))     # Expected output: 500
    print(sol.maximumProduct([-1, -2, -3]))         # Expected output: -6