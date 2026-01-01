from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is height-balanced.
        """

        def dfs(node):
            # Base case: empty subtree
            if not node:
                return True, 0

            # ---------- Postorder traversal ----------
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            # Check balance condition
            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            # Return balance status and height
            return balanced, 1 + max(left_height, right_height)

        return dfs(root)[0]
