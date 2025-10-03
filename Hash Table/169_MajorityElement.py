"""
LeetCode 169: Majority Element
https://leetcode.com/problems/majority-element/

Approach: Boyer–Moore Voting Algorithm
- Keep track of a candidate and a counter.
- Reset candidate when counter is 0.
- Increase counter if current element == candidate, otherwise decrease.
- Guaranteed that the final candidate is the majority element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))       # Expected output: 3
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Expected output: 2
