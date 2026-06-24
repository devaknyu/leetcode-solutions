"""
LeetCode 167: Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Approach:
- Find two numbers that add up to target in sorted array
- Return 1-based indices of the two numbers
- Use two pointers since array is sorted

Space Complexity Analysis:
- Yes, this solution has O(1) space complexity
- Only using fixed variables (l, r) - no extra data structures
- Input array is already sorted, no additional storage needed

Technique: Two Pointers
1. Left pointer at start, right pointer at end
2. If sum equals target, return indices (1-based)
3. If sum > target, move right pointer left
4. If sum < target, move left pointer right

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only constant extra space used
"""

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l + 1, r + 1]  # 1-based indices
            elif current_sum > target:
                r -= 1
            else:  # current_sum < target
                l += 1
        return []


# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),   # → [1, 2]
        ([2, 3, 4], 6),        # → [1, 3]
        ([-1, 0], -1),         # → [1, 2]
        ([1, 2, 3, 4], 7),     # → [3, 4]
    ]
    
    for numbers, target in test_cases:
        print(f"numbers={numbers}, target={target}")
        result = sol.twoSum(numbers, target)
        print(f"Output: {result}\n")