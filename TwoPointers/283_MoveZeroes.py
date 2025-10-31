"""
LeetCode 283: Move Zeroes
https://leetcode.com/problems/move-zeroes/

Approach:
- We are asked to move all zeroes in the array to the end while maintaining the relative order of non-zero elements.
- The operation must be done **in-place**, without making a copy of the array.

Two-pointer approach:
1. Use two pointers — `l` (left) and `r` (right):
   - `l` points to the position where the next non-zero element should be placed.
   - `r` scans through each element of the array.
2. When `nums[r]` is non-zero:
   - Swap elements at positions `l` and `r`.
   - Increment `l` (since we’ve placed one more non-zero in its correct spot).
3. When `nums[r]` is zero:
   - Do nothing, just move `r` forward.
4. Continue until the end of the array.

By the end, all non-zero elements will be shifted to the front, and all zeroes will be moved to the back.

Example:
Input:
  nums = [0,1,0,3,12]
Process:
  → [1,0,0,3,12]
  → [1,3,0,0,12]
  → [1,3,12,0,0]
Output:
  [1,3,12,0,0]

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
        return nums

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0, 1, 0, 3, 12]))  # Expected output: [1, 3, 12, 0, 0]
    print(sol.moveZeroes([0, 0, 1]))         # Expected output: [1, 0, 0]
    print(sol.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))  # Expected output: [4,2,4,3,5,1,0,0,0,0]