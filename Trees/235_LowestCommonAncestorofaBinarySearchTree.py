"""
LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Problem Description:
- Given a Binary Search Tree (BST) and two nodes p and q,
  find their lowest common ancestor (LCA).
- The LCA of two nodes p and q is defined as the lowest node
  in the tree that has both p and q as descendants
  (where a node can be a descendant of itself).

BST Property:
- Left subtree values < node value
- Right subtree values > node value

Approach:
- Start from the root and traverse the tree iteratively.
- Use the BST property to decide whether to move left or right:
  - If both p and q are smaller than the current node,
    the LCA lies in the left subtree.
  - If both p and q are greater than the current node,
    the LCA lies in the right subtree.
  - Otherwise, the current node is the split point
    and hence the LCA.

Key Observations:
- Since it is a BST, we do not need to explore both subtrees.
- The first node where p and q diverge is the LCA.
- Iterative traversal avoids recursion stack overhead.

Technique: Iterative BST Traversal
1. Initialize a pointer at the root
2. Compare current node value with p and q
3. Move left or right accordingly
4. Return the node where paths diverge

Time Complexity:
- O(h), where h is the height of the BST
  (O(log n) for balanced BST, O(n) for skewed BST)

Space Complexity:
- O(1), since the solution is iterative
"""

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

