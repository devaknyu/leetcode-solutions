from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Returns True if two binary trees are structurally identical
        and have the same node values.
        """

        # Both nodes are None
        if not p and not q:
            return True

        # One node is None or values differ
        if not p or not q or p.val != q.val:
            return False

        # Recursively compare subtrees
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
