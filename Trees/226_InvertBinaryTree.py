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

# Example usage
if __name__ == "__main__":
    # Helper function to print tree in level order
    from collections import deque

    def print_tree(root):
        if not root:
            print([])
            return
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)
        print(result)

    # Example
    # Input tree:
    #       4
    #     /   \
    #    2     7
    #   / \   / \
    #  1   3 6   9

    root = TreeNode(4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9))
        )

    inverted = Solution().invertTree(root)
    print_tree(inverted)
    # Expected output (level order):
    # [4, 7, 2, 9, 6, 3, 1]