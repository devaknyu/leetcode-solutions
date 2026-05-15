from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Returns True if subRoot is a subtree of root.
        """

        # An empty tree is always a subtree
        if not subRoot:
            return True

        # If main tree is empty but subtree is not
        if not root:
            return False

        # Check if trees match at current node
        if self.isSame(root, subRoot):
            return True

        # Otherwise, search left and right subtrees
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def isSame(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        """
        Checks if two binary trees are identical.
        """

        if not r and not s:
            return True

        if not r or not s or r.val != s.val:
            return False

        return (
            self.isSame(r.left, s.left) and
            self.isSame(r.right, s.right)
        )
