"""
LeetCode 219: Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Approach:
- Use a sliding window of size `k` to track recently seen elements using a set.
- Iterate through the list with a right pointer (R):
  - If the window size exceeds `k`, remove the leftmost element (nums[L]) and increment L.
  - If nums[R] is already in the window, return True (duplicate found within distance k).
  - Otherwise, add nums[R] to the window.
- Return False if no such duplicates are found.

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))   # Expected output: True
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))   # Expected output: True
    print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Expected output: False