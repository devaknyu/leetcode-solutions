"""
LeetCode 199: Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Problem Description:
- Given the root of a binary tree,
  return the values of the nodes that are visible from the right side.
- You must return one node from each level:
  the rightmost node at that depth.

Approach:
- Use Breadth-First Search (BFS) to traverse the tree level by level.
- Maintain a queue to process all nodes of the current level.
- While processing a level:
  - Keep updating a pointer to the most recently seen node.
  - Since nodes are dequeued from left to right,
    the last valid node processed will be the rightmost one.
- Append that node’s value to the result list.

Key Observations:
- Only one node per level is required in the output.
- BFS ensures natural left-to-right ordering.
- Tracking the last node of each level gives the correct view.
- Null nodes must be ignored during traversal.

Technique: BFS with Level Tracking
1. Initialize an empty result list
2. Push the root node into the queue
3. While the queue is not empty:
   - Record the current queue length (level size)
   - Process all nodes of that level
   - Track the last non-null node
   - Append its value to the result
4. Return the final list of visible nodes

Time Complexity:
- O(n), where n is the number of nodes in the tree
  (each node is visited exactly once)

Space Complexity:
- O(n), due to storage in the BFS queue
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the list of node values visible from the right side.
        """

        res = []

        # Edge case: empty tree
        if not root:
            return res

        q = collections.deque([root])

        while q:
            rightside = None
            qlen = len(q)

            for _ in range(qlen):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)

            if rightside:
                res.append(rightside.val)

        return res

# Example usage
if __name__ == "__main__":
    """
        Tree:
            1
           / \
          2   3
           \    \
            5    4
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    print(Solution().rightSideView(root))
    # Expected Output: [1, 3, 4]