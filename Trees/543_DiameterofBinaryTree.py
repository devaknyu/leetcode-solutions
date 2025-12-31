"""
LeetCode 543: Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Problem Description:
- Given the root of a binary tree, return the length of its diameter.
- The diameter is the length of the longest path between any two nodes in the tree.
- This path may or may not pass through the root.
- The length of a path is measured by the number of edges between nodes.

Approach:
- Use Depth-First Search (DFS) to compute subtree heights.
- At each node:
  1. Compute the height of its left subtree
  2. Compute the height of its right subtree
  3. Update the global diameter using left_height + right_height
- Return the height of the subtree to the parent.

Key Observations:
- The diameter at a node equals the sum of the heights of its left and right subtrees.
- The maximum diameter can occur at any node, not just the root.
- Height is computed bottom-up, while diameter is updated globally.

Technique: Depth-First Search (DFS) + Postorder Traversal
1. Traverse the tree recursively
2. For each node, compute left and right subtree heights
3. Update the maximum diameter
4. Return subtree height to parent

Time Complexity:
- O(n), where n is the number of nodes in the tree

Space Complexity:
- O(h), where h is the height of the tree (recursion stack)
  - Worst case: O(n)
  - Best case: O(log n)
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Returns the diameter of a binary tree.
        """

        self.res = 0

        def dfs(node):
            # Base case: empty subtree
            if not node:
                return 0

            # ---------- Postorder traversal ----------
            left = dfs(node.left)
            right = dfs(node.right)

            # Update diameter
            self.res = max(self.res, left + right)

            # Return height of subtree
            return 1 + max(left, right)

        dfs(root)
        return self.res

# Example usage
if __name__ == "__main__":
    # Build tree
    root = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3)
        )

    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    diameter = Solution().diameterOfBinaryTree(root)
    print(diameter)  # Expected: 3
