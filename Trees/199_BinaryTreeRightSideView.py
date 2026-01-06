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