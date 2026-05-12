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

# Example usage
if __name__ == "__main__":
    # Identical trees
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

    # Different trees
    tree3 = TreeNode(1, TreeNode(2))
    tree4 = TreeNode(1, None, TreeNode(2))

    print(Solution().isSameTree(tree1, tree2))  # Expected: True
    print(Solution().isSameTree(tree3, tree4))  # Expected: False