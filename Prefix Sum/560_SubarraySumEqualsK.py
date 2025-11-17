from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0: 1}  # Base case: sum 0 appears once

        for n in nums:
            curSum += n
            diff = curSum - k  # We've seen this prefix sum before
            
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            
        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1,1,1], 2),     # → 2
        ([1,2,3], 3),     # → 2
        ([1,-1,0], 0),    # → 3
        ([1], 0),         # → 0
    ]
    
    for nums, k in test_cases:
        print(f"nums={nums}, k={k} → {sol.subarraySum(nums, k)}")