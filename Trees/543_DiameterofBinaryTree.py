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
