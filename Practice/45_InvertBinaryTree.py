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