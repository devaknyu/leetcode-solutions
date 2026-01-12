"""
LeetCode 297: Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Problem Description:
- Design an algorithm to serialize and deserialize a binary tree.
- Serialization converts a binary tree into a string.
- Deserialization reconstructs the binary tree from the string.
- The encoded string must allow complete reconstruction of the tree.
- There is no restriction on the format as long as it is reversible.

Approach:
- Use Depth-First Search (DFS) with preorder traversal.
- While serializing:
  - Record node values.
  - Use a sentinel (e.g., "N") to represent null nodes.
- While deserializing:
  - Rebuild the tree by reading values sequentially.
  - When a sentinel is encountered, return None.

Key Observations:
- Preorder traversal preserves root placement.
- Explicitly storing null nodes is required to maintain structure.
- A shared index allows correct reconstruction order.
- The serialization format must match the deserialization logic.

Technique: DFS Preorder Serialization
1. Traverse the tree using preorder DFS
2. Append node values to a list
3. Append a sentinel for null nodes
4. Join the list into a string
5. During deserialization, read values in order
6. Rebuild left and right subtrees recursively

Time Complexity:
- O(n), where n is the number of nodes
  (each node is processed once)

Space Complexity:
- O(n), due to storage of serialized string
  and recursion stack
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        Encodes a binary tree into a string.
        """

        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """
        Decodes a serialized string back into a binary tree.
        """

        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Example usage
if __name__ == "__main__":
    """
        Tree:
            1
           / \
          2   3
             / \
            4   5
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ser = Codec()
    deser = Codec()

    data = ser.serialize(root)
    print("Serialized:", data)

    restored = deser.deserialize(data)
    print("Restored Root:", restored.val)  # Expected: 1