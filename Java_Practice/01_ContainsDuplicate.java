/*
LeetCode 217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Approach:

- Use a HashSet to store all unique elements.
- Iterate through each number in the array:
  - Add each number to the HashSet.
- After processing all elements:
  - If the size of the HashSet is smaller than the length of the array,
    duplicates exist, so return true.
  - Otherwise, return false.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> res = new HashSet<>();
        for (int n: nums){
            res.add(n);
        }
        return res.size() != nums.length;
    }


    // Example usage
    public static void main(String[] args) {

        Solution sol = new Solution();

        System.out.println(sol.containsDuplicate(new int[]{1, 2, 3, 1}));
        // Expected output: true

        System.out.println(sol.containsDuplicate(new int[]{1, 2, 3, 4}));
        // Expected output: false

        System.out.println(sol.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));
        // Expected output: true
    }
}