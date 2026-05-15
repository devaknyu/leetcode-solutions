"""
LeetCode 102: Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem Description:
- Given the root of a binary tree,
  return the level order traversal of its nodes' values.
- Level order traversal means visiting nodes level by level,
  from left to right.

Approach:
- Use Breadth-First Search (BFS) to traverse the tree.
- Maintain a queue to process nodes level by level.
- For each level:
  - Record the number of nodes currently in the queue.
  - Process exactly that many nodes to form one level.
  - Add their children to the queue for the next level.

Key Observations:
- BFS naturally processes nodes in level order.
- Tracking the queue size allows clean separation of levels.
- Null nodes should be ignored to avoid incorrect values.

Technique: Breadth-First Search (BFS) using Queue
1. Initialize an empty result list
2. Push the root into the queue
3. While the queue is not empty:
   - Determine the current level size
   - Process all nodes of the current level
   - Append their values to a level list
   - Add children to the queue
4. Append each level list to the result

Time Complexity:
- O(n), where n is the number of nodes in the tree
  (each node is visited exactly once)

Space Complexity:
- O(n), due to the queue storing up to one full level of nodes
"""

from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Returns the level order traversal of a binary tree.
        """

        res = []

        # Edge case: empty tree
        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            lvl = []
            lenq = len(q)

            for _ in range(lenq):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(lvl)

        return res

# Example usage
if __name__ == "__main__":
    """
        Tree:
            3
           / \
          9  20
             / \
            15  7
    """

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().levelOrder(root))
    # Expected: [[3], [9, 20], [15, 7]]