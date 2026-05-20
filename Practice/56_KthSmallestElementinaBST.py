from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Returns the kth smallest element in a BST.
        """

        n = 0
        stack = []
        cur = root

        while cur or stack:
            # Go to the leftmost node
            while cur:
                stack.append(cur)
                cur = cur.left

            # Process the node
            cur = stack.pop()
            n += 1

            if n == k:
                return cur.val

            # Visit right subtree
            cur = cur.right

# Example usage
if __name__ == "__main__":
    """
        BST:
              5
             / \
            3   6
           / \
          2   4
         /
        1
    """

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    print(Solution().kthSmallest(root, 3))  # Expected: 3