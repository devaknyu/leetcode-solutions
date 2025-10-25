"""
LeetCode 455: Assign Cookies
https://leetcode.com/problems/assign-cookies/

Approach:
- Each child `i` has a greed factor `g[i]`, and each cookie `j` has a size `s[j]`.
- A child is content if `s[j] >= g[i]`.
- The goal is to maximize the number of content children by distributing cookies efficiently.

Steps:
1. Sort both `g` (children's greed) and `s` (cookie sizes) in ascending order.
2. Use two pointers:
   - `i` → current child.
   - `j` → current cookie.
3. Iterate through the cookies:
   - If `s[j]` satisfies `g[i]`, assign it and move both pointers (`i += 1`, `j += 1`).
   - Otherwise, move only `j` to check the next larger cookie.
4. Stop when all cookies are used or all children are satisfied.
5. The number of content children is given by `i`.

Example:
Input:
  g = [1, 2, 3], s = [1, 1]
Output:
  1
Explanation:
  Only one child (greed 1) can be satisfied with one cookie (size 1).

Time Complexity: O(n log n) — due to sorting
Space Complexity: O(1)
"""

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0

        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j < len(s):
                i += 1
                j += 1
            else:
                break
        return i

# Example usage
    if __name__ == "__main__":
        sol = Solution()
        print(sol.findContentChildren([1, 2, 3], [1, 1]))   # Expected output: 1
        print(sol.findContentChildren([1, 2], [1, 2, 3]))   # Expected output: 2
        print(sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))  # Expected output: 2