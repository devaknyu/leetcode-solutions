"""
LeetCode 100: Same Tree
https://leetcode.com/problems/same-tree/

Problem Description:
- Given the roots of two binary trees p and q,
  determine if they are the same.
- Two binary trees are considered the same if:
  * They have the same structure
  * Corresponding nodes have the same values

Approach:
- Use recursion to traverse both trees simultaneously.
- At each step:
  1. Check if both nodes are None → trees match so far
  2. If only one node is None or values differ → trees are not the same
  3. Recursively compare left and right subtrees

Key Observations:
- Structure and node values must match exactly.
- Comparing nodes in the same traversal order is essential.
- The problem naturally fits a recursive DFS solution.

Technique: Depth-First Search (DFS) + Recursion
1. Traverse both trees in parallel
2. Compare current node values
3. Recursively compare left children
4. Recursively compare right children
5. If all checks pass, trees are identical

Time Complexity:
- O(n), where n is the number of nodes in the smaller tree

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