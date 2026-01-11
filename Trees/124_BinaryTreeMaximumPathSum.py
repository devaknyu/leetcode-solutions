"""
LeetCode 124: Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem Description:
- Given the root of a binary tree,
  return the maximum path sum.
- A path can start and end at any node.
- The path must contain at least one node.
- The path does not need to pass through the root.

Approach:
- Use Depth-First Search (DFS) to compute path sums.
- At each node:
  - Compute the maximum gain from the left subtree.
  - Compute the maximum gain from the right subtree.
- Ignore negative gains since they reduce the total sum.
- Update a global result to track the best path seen so far.

Key Observations:
- A path can go through a node using both left and right children.
- However, when returning to the parent, only one side can be used.
- Negative paths should be discarded (treated as 0).
- A global variable is needed to track the maximum across all nodes.

Technique: DFS with Global Maximum Tracking
1. Perform DFS traversal
2. For each node, compute left and right subtree gains
3. Discard negative gains using max(0, gain)
4. Update global maximum with:
   node.val + leftGain + rightGain
5. Return node.val + max(leftGain, rightGain) to parent

Time Complexity:
- O(n), where n is the number of nodes
  (each node is visited once)

Space Complexity:
- O(h), where h is the height of the tree
  (recursion stack)
"""


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
