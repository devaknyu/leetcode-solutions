"""
LeetCode 230: Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem Description:
- Given the root of a Binary Search Tree (BST)
  and an integer k,
  return the kth smallest value among all nodes.
- The BST property guarantees that an inorder traversal
  visits nodes in ascending order.

Approach:
- Use iterative inorder traversal (Left → Node → Right).
- Inorder traversal of a BST produces values in sorted order.
- Maintain a counter to track how many nodes have been visited.
- When the counter reaches k, return the current node’s value.

Key Observations:
- Recursion is not required; a stack simulates the call stack.
- Early termination is possible once the kth element is found.
- This approach avoids storing the full inorder list.

Technique: Iterative Inorder Traversal (DFS)
1. Initialize an empty stack and set current node to root
2. Traverse left until reaching a null node
3. Pop from the stack and process the node
4. Increment count
5. If count equals k, return the node value
6. Move to the right subtree
7. Repeat until k is found

Time Complexity:
- O(h + k), where h is the height of the tree
  (worst case O(n) if the tree is skewed)

Space Complexity:
- O(h), due to the stack used for traversal
"""

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