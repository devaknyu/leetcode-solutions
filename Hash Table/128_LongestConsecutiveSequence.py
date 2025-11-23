from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            # Check if this is the start of a sequence
            if (num - 1) not in numSet:
                length = 0
                # Count consecutive numbers
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [100, 4, 200, 1, 3, 2],  # → 4 (1,2,3,4)
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],  # → 9 (0,1,2,3,4,5,6,7,8)
        [1, 0, -1],  # → 3 (-1,0,1)
        [],  # → 0
        [1, 3, 5],  # → 1
    ]
    
    for nums in test_cases:
        print(f"Input:  {nums}")
        result = sol.longestConsecutive(nums)
        print(f"Output: {result}\n")