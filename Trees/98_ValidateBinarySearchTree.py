from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is a valid BST.
        """

        def dfs(node: Optional[TreeNode], left: float, right: float) -> bool:
            if not node:
                return True

            # Validate current node value
            if not (left < node.val < right):
                return False

            # Recursively validate subtrees with updated bounds
            return (
                dfs(node.left, left, node.val) and
                dfs(node.right, node.val, right)
            )

        return dfs(root, float("-inf"), float("inf"))