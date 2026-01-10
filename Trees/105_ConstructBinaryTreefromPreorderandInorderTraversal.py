from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Constructs and returns the binary tree from preorder
        and inorder traversal lists.
        """

        if not preorder or not inorder:
            return None

        # Root is always the first element of preorder
        root = TreeNode(preorder[0])

        # Find root index in inorder traversal
        mid = inorder.index(preorder[0])

        # Build left and right subtrees
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        return root

# Example usage
if __name__ == "__main__":
    """
        preorder = [3, 9, 20, 15, 7]
        inorder  = [9, 3, 15, 20, 7]

        Tree:
            3
           / \
          9  20
             / \
            15  7
    """

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = Solution().buildTree(preorder, inorder)
    print(root.val)  # Expected: 3
