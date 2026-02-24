class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        numMax, numMin = 1, 1

        for n in nums:
            tmp = numMax * n
            numMax = max(numMax * n, numMin * n, n)
            numMin = min(tmp, numMin * n, n)
            res = max(res, numMax)

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))  # Expected: 6
    print(sol.maxProduct([-2, 0, -1]))    # Expected: 0
    print(sol.maxProduct([-2, 3, -4]))    # Expected: 24