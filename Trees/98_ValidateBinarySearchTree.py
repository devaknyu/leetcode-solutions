"""
LeetCode 98: Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Problem Description:
- Given the root of a binary tree,
  determine if it is a valid Binary Search Tree (BST).
- A valid BST must satisfy:
  - All values in the left subtree are strictly less than the node value
  - All values in the right subtree are strictly greater than the node value
  - Both left and right subtrees must also be valid BSTs

Approach:
- Use Depth-First Search (DFS) with value bounds.
- For each node, maintain a valid range (left, right):
  - The node value must lie strictly between these bounds.
- Recursively validate left and right subtrees by updating bounds:
  - Left subtree: upper bound becomes current node value
  - Right subtree: lower bound becomes current node value

Key Observations:
- Checking only parent-child relationships is insufficient.
- Each node must respect constraints imposed by all its ancestors.
- Passing bounds ensures global BST validity.
- Strict inequalities are required (no duplicates allowed).

Technique: DFS with Range Validation
1. Start DFS from the root with range (-∞, +∞)
2. At each node, verify its value lies within the range
3. Recursively validate left subtree with updated upper bound
4. Recursively validate right subtree with updated lower bound
5. If all nodes satisfy constraints, return True

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is a valid BST.
        """

        def dfs(node: Optional[TreeNode], left: float, right: float) -> bool:
            if not node:
                return True

            # Validate current node value
            if not (left < node.val < right):
                return False

            # Recursively validate subtrees with updated bounds
            return (
                dfs(node.left, left, node.val) and
                dfs(node.right, node.val, right)
            )

        return dfs(root, float("-inf"), float("inf"))

# Example usage
if __name__ == "__main__":
    """
        Valid BST:
            2
           / \
          1   3
    """

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(Solution().isValidBST(root))  # Expected: True