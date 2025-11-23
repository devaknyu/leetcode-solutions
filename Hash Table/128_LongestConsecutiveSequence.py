
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