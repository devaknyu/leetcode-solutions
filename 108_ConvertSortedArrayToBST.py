"""
LeetCode 108: Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Problem:
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree (BST).

Definition of height-balanced BST:
- A binary tree is height-balanced if the depth of the two subtrees of every node never differs by more than 1.

Approach:
- Use a divide-and-conquer strategy.
- Pick the middle element of the current subarray as the root (to keep balance).
- Recursively build the left subtree from the left half, and the right subtree from the right half.
- Base case: if l > r, return None.

Time Complexity: O(n)   (each element is visited once)
Space Complexity: O(log n)  (recursion stack in a balanced tree)
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper_fun(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper_fun(l, m - 1)
            root.right = helper_fun(m + 1, r)
            return root

        return helper_fun(0, len(nums) - 1)
    
    # Example run for local testing
def preorder_traversal(root: Optional[TreeNode]):
    """ Helper to print preorder traversal of the BST. """
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    bst_root = Solution().sortedArrayToBST(nums)
    print(preorder_traversal(bst_root))  # Example output: [0, -10, -3, 5, 9]
