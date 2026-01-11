from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum path sum in the binary tree.
        """

        # Global maximum path sum (stored as list for mutability)
        res = [root.val]

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Compute max gain from left and right subtrees
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # Ignore negative contributions
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update global maximum using both children
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # Return max gain including current node
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
    
# Example usage
if __name__ == "__main__":
    """
        Tree:
             -10
             /  \
            9   20
               / \
              15  7

        Maximum Path Sum = 15 + 20 + 7 = 42
    """

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().maxPathSum(root))  # Expected: 42
