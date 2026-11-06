"""
LeetCode 226: Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Problem Description:
- Given the root of a binary tree, invert the tree.
- Inverting means swapping the left and right children of every node.

Approach:
- Use recursion to traverse the tree.
- At each node:
  1. Swap its left and right children
  2. Recursively invert the left subtree
  3. Recursively invert the right subtree

Key Observations:
- The operation must be applied to every node.
- A recursive depth-first traversal naturally fits the problem.
- The inversion of a tree is symmetric at every node.

Technique: Depth-First Search (DFS) + Recursion
1. Base case: if the current node is None, return
2. Swap left and right child pointers
3. Recursively apply the same operation on subtrees
4. Return the root after inversion

Time Complexity:
- O(n), where n is the number of nodes in the tree

Space Complexity:
- O(h), where h is the height of the tree (recursion stack)
  - Worst case: O(n) for a skewed tree
  - Best case: O(log n) for a balanced tree
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by recursively swapping
        left and right subtrees.
        """

        # Base case
        if not root:
            return None

        # ---------- Step 1: Swap children ----------
        root.left, root.right = root.right, root.left

        # ---------- Step 2: Recurse on subtrees ----------
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Example usage
if __name__ == "__main__":
    # Helper function to print tree in level order
    from collections import deque

    def print_tree(root):
        if not root:
            print([])
            return
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)
        print(result)

    # Example
    # Input tree:
    #       4
    #     /   \
    #    2     7
    #   / \   / \
    #  1   3 6   9

    root = TreeNode(4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9))
        )

    inverted = Solution().invertTree(root)
    print_tree(inverted)
    # Expected output (level order):
    # [4, 7, 2, 9, 6, 3, 1]