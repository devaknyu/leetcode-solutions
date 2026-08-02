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