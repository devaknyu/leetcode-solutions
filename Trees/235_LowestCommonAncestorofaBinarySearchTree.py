# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        """
        Returns the lowest common ancestor (LCA) of nodes p and q
        in a Binary Search Tree.
        """

        cur = root

        while cur:
            # Both nodes lie in the left subtree
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left

            # Both nodes lie in the right subtree
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right

            # Split point found — this is the LCA
            else:
                return cur
