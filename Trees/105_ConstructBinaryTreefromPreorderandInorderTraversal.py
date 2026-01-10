"""
LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem Description:
- Given two integer arrays preorder and inorder,
  construct and return the binary tree.
- preorder traversal visits nodes in the order:
  Root → Left → Right
- inorder traversal visits nodes in the order:
  Left → Root → Right
- All node values are unique.

Approach:
- The first element in preorder is always the root.
- Find the root value’s index in the inorder array.
- Elements to the left of the root in inorder form the left subtree.
- Elements to the right form the right subtree.
- Recursively apply the same logic to build left and right subtrees.

Key Observations:
- preorder determines the root at each recursive step.
- inorder determines the boundary between left and right subtrees.
- Array slicing simplifies logic but introduces extra overhead.
- This solution is easy to understand but not optimal in time.

Technique: Recursive Tree Construction
1. Base case: if preorder or inorder is empty, return None
2. Create the root using the first element of preorder
3. Locate the root in inorder to split left and right subtrees
4. Recursively construct left subtree
5. Recursively construct right subtree
6. Return the constructed root

Time Complexity:
- O(n²) in the worst case
  (each inorder.index call is O(n) inside recursion)

Space Complexity:
- O(n), due to recursion stack and array slicing
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Constructs and returns the binary tree from preorder
        and inorder traversal lists.
        """

        if not preorder or not inorder:
            return None

        # Root is always the first element of preorder
        root = TreeNode(preorder[0])

        # Find root index in inorder traversal
        mid = inorder.index(preorder[0])

        # Build left and right subtrees
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        return root

# Example usage
if __name__ == "__main__":
    """
        preorder = [3, 9, 20, 15, 7]
        inorder  = [9, 3, 15, 20, 7]

        Tree:
            3
           / \
          9  20
             / \
            15  7
    """

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = Solution().buildTree(preorder, inorder)
    print(root.val)  # Expected: 3
