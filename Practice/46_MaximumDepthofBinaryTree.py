"""
LeetCode 104: Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem Description:
- Given the root of a binary tree, return its maximum depth.
- The maximum depth is the number of nodes along the longest path
  from the root node down to the farthest leaf node.

Approach:
- Use recursion to explore both left and right subtrees.
- At each node, compute the depth of its subtrees.
- The depth of a node is 1 plus the maximum depth of its children.

Key Observations:
- A leaf node has a depth of 1.
- An empty tree has a depth of 0.
- The problem naturally fits a recursive DFS solution.

Technique: Depth-First Search (DFS) + Recursion
1. Base case: if the current node is None, return 0
2. Recursively compute depth of left subtree
3. Recursively compute depth of right subtree
4. Return 1 + max(left_depth, right_depth)

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum depth of a binary tree.
        """

        # Base case: empty tree
        if not root:
            return 0

        # ---------- Recursive DFS ----------
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )

# Example usage
if __name__ == "__main__":
    # Helper function to build a binary tree
    root = TreeNode(3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
        )

    # Tree structure:
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7

    depth = Solution().maxDepth(root)
    print(depth)  # Expected: 3