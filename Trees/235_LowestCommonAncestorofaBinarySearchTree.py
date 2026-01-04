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
            
# Example usage
if __name__ == "__main__":
    """
        BST:
              6
             / \
            2   8
           / \ / \
          0  4 7  9
            / \
           3   5
    """

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.left        # Node 2
    q = root.left.right  # Node 4

    lca = Solution().lowestCommonAncestor(root, p, q)
    print(lca.val)  # Expected: 2

