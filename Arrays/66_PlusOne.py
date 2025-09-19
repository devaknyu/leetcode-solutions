"""
LeetCode 66: Plus One
https://leetcode.com/problems/plus-one/

Problem:
You are given a large integer represented as an integer array `digits`, 
where each `digits[i]` is the ith digit of the integer. 
Increment the large integer by one and return the resulting array of digits.

Approach:
- Traverse digits from right to left.
- If current digit + 1 != 10 → just increment and return.
- If current digit + 1 == 10 → set digit to 0 and continue.
- If we finish the loop with carry (like 999 → 1000), prepend 1 at the front.

Time Complexity: O(n)   (single pass through digits)
Space Complexity: O(1)  (in-place, ignoring output array)
"""


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        # If all digits were 9 → [9,9,9] → [1,0,0,0]
        return [1] + digits
    
    # Example run for local testing
if __name__ == "__main__":
    print(Solution().plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(Solution().plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]