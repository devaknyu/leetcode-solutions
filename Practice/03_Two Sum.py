"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/

Approach:
- Find two numbers that add up to the target
- Return the indices of the two numbers
- Use a hash map to store previously seen numbers and their indices

Space Complexity Analysis:
- This solution has O(n) space complexity
- The hash map (seen) stores up to n elements in the worst case
- Extra memory is required to achieve O(n) time complexity

Technique: Hash Map
1. Iterate through the array
2. Compute the complement (target - current number)
3. Check if the complement has already been seen
4. If yes, return the stored index and current index
5. Otherwise, store the current number and its index

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map stores previously seen elements
"""

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[num] = i
        return

# Example usage
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),      # → [0, 1]
        ([3, 2, 4], 6),           # → [1, 2]
        ([3, 3], 6),              # → [0, 1]
        ([1, 5, 3, 7], 8),        # → [0, 3]
    ]

    for nums, target in test_cases:
        print(f"nums={nums}, target={target}")
        result = sol.twoSum(nums, target)
        print(f"Output: {result}\n")