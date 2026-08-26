"""
LeetCode 217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Approach:
- Use a set to keep track of elements seen so far.
- Iterate through each number in the list:
  - If the number is already in the set, return True (duplicate found).
  - Otherwise, add it to the set.
- If the loop completes with no duplicates, return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # Expected output: True
    print(sol.containsDuplicate([1, 2, 3, 4]))  # Expected output: False
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Expected output: True