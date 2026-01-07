"""
LeetCode 1448: Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Problem Description:
- Given the root of a binary tree,
  count the number of "good" nodes.
- A node X in the tree is considered good if,
  in the path from the root to X,
  there are no nodes with a value greater than X.

Approach:
- Use Depth-First Search (DFS) to traverse the tree.
- While traversing, keep track of the maximum value seen so far
  along the current root-to-node path.
- For each node:
  - If its value is greater than or equal to max-so-far,
    it qualifies as a good node.
  - Update the max value for the recursive calls to its children.

Key Observations:
- The definition of a good node depends only on values in its path.
- We do not need to store the entire path—only the maximum value.
- DFS is ideal since we explore paths from root to leaves.
- The problem can be solved cleanly with a helper recursive function.

Technique: DFS with Path Maximum Tracking
1. Start DFS traversal from the root
2. Pass the current maximum value to each recursive call
3. At each node, check if it is a good node
4. Update maximum and continue traversal
5. Sum good nodes from left and right subtrees

Time Complexity:
- O(n), where n is the number of nodes
  (each node is visited exactly once)

Space Complexity:
- O(h), where h is the height of the tree
  (recursion stack depth)
"""


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