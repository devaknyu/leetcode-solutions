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