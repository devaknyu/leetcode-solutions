"""
LeetCode 704: Binary Search
https://leetcode.com/problems/binary-search/

Approach:
- Search for target in sorted array using binary search
- Narrow search range by half each iteration
- Return index if found, -1 if not found

Technique: Classic Binary Search
1. Initialize left and right pointers
2. Calculate middle index
3. Compare middle element with target
4. Adjust left or right pointer based on comparison
5. Continue until target found or search space exhausted

Time Complexity: O(log n) - halves search space each iteration
Space Complexity: O(1) - only constant extra space
"""

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
                
        return -1
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),   # → 4
        ([-1, 0, 3, 5, 9, 12], 2),   # → -1
        ([5], 5),                     # → 0
        ([1, 3, 5, 7, 9], 1),        # → 0
    ]
    
    for nums, target in test_cases:
        print(f"nums={nums}, target={target}")
        result = sol.search(nums, target)
        print(f"Index: {result}\n")