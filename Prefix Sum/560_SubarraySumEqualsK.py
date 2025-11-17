"""
LeetCode 560: Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Approach:
- Count subarrays where sum equals k using prefix sums
- Track cumulative sum frequencies in hash map
- If prefixSum - k exists in map, we found subarrays summing to k

Technique: Prefix Sum with Hash Map
1. Track running sum and count its frequency
2. For each number, check if (currentSum - k) exists in map
3. Each occurrence of (currentSum - k) represents a valid subarray
4. Update frequency of current sum

Time Complexity: O(n)
Space Complexity: O(n) for prefix sums map
"""


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