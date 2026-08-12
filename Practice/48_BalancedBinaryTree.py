"""
LeetCode 110: Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Problem Description:
- Given a binary tree, determine if it is height-balanced.
- A binary tree is balanced if:
  * The left and right subtrees of every node differ in height by no more than 1.

Approach:
- Use Depth-First Search (DFS) to compute subtree heights.
- At each node:
  1. Check if left subtree is balanced
  2. Check if right subtree is balanced
  3. Verify the height difference is ≤ 1
- Return both balance status and height together.

Key Observations:
- Height information is required to determine balance.
- Checking balance top-down would be inefficient.
- Combining balance check and height calculation in one DFS pass is optimal.

Technique: Depth-First Search (DFS) + Postorder Traversal
1. Traverse the tree bottom-up
2. For each node, gather:
   - Whether left subtree is balanced
   - Whether right subtree is balanced
   - Heights of left and right subtrees
3. Compute balance condition
4. Return balance status and subtree height

Time Complexity:
- O(n), where n is the number of nodes in the tree

Space Complexity:
- O(h), where h is the height of the tree (recursion stack)
  - Worst case: O(n)
  - Best case: O(log n)
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is height-balanced.
        """

        def dfs(node):
            # Base case: empty subtree
            if not node:
                return True, 0

            # ---------- Postorder traversal ----------
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            # Check balance condition
            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            # Return balance status and height
            return balanced, 1 + max(left_height, right_height)

        return dfs(root)[0]

# Example usage
if __name__ == "__main__":
    # Balanced tree example
    balanced_root = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )

    # Unbalanced tree example
    unbalanced_root = TreeNode(1,
        TreeNode(2,
            TreeNode(3,
                TreeNode(4),
                None
            ),
            None
        ),
        None
    )

    print(Solution().isBalanced(balanced_root))    # Expected: True
    print(Solution().isBalanced(unbalanced_root))  # Expected: False