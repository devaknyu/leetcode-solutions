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