from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        # Iterate over numSet instead of nums to avoid duplicate processing
        for num in numSet:
            # Check if this is the start of a sequence
            if (num - 1) not in numSet:
                length = 1
                # Count consecutive numbers
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

