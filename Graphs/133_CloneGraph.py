from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            # Return existing clone if already visited
            if node in oldToNew:
                return oldToNew[node]

            # Create clone
            copy = Node(node.val)
            oldToNew[node] = copy

            # Clone neighbors
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))

            return copy

        return dfs(node) if node else None
