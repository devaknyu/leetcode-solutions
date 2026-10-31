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