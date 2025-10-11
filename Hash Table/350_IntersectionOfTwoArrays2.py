"""
LeetCode 350: Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Approach:
- Unlike LeetCode 349, this problem allows duplicate elements in the intersection.
- We can solve it efficiently using a hash map (dictionary) to count the occurrences of each number in `nums1`.
- Then, iterate through `nums2`:
  - If the current number exists in the dictionary and its count is greater than 0,
    add it to the result list and decrement its count by 1.
- This ensures each element is included only as many times as it appears in both arrays.

Example:
nums1 = [1, 2, 2, 1], nums2 = [2, 2] → [2, 2]
nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4] → [4, 9]

Time Complexity: O(n + m)
Space Complexity: O(min(n, m)) — for storing counts of the smaller array
"""

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count = {}
        result = []

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        
        return result
    
    # Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1, 2, 2, 1], [2, 2]))          # Expected output: [2, 2]
    print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))    # Expected output: [9, 4]