from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Returns the count of good nodes in the binary tree.
        """

        def dfs(node: Optional[TreeNode], maxval: int) -> int:
            if not node:
                return 0

            # Check if current node is good
            res = 1 if node.val >= maxval else 0

            # Update max value for children
            maxval = max(maxval, node.val)

            # Continue DFS traversal
            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)

            return res

        return dfs(root, root.val)


# Example usage
if __name__ == "__main__":
    """
        Tree:
            3
           / \
          1   4
         /   / \
        3   1   5
    """

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    print(Solution().goodNodes(root))  # Example Output