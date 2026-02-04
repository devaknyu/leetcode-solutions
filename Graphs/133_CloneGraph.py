"""
LeetCode 133: Clone Graph
https://leetcode.com/problems/clone-graph/

Problem Description:
- Given a reference to a node in a connected undirected graph,
  return a deep copy (clone) of the graph.
- Each node contains a value and a list of its neighbors.
- The graph may contain cycles.
- The given node may be None.

Approach:
- Use Depth-First Search (DFS) to traverse the graph.
- Maintain a hash map that maps original nodes to their cloned copies.
- Whenever a node is visited:
  - If it is already cloned, return the clone.
  - Otherwise, create a new node and recursively clone its neighbors.

Key Observations:
- Graphs can contain cycles → naive DFS would loop infinitely.
- The hashmap (old → new) prevents repeated cloning.
- Each node is cloned exactly once.
- Neighbor relationships are rebuilt during recursion.

Technique: Graph DFS with Hash Map
1. If the input node is None, return None.
2. Start DFS from the given node.
3. If a node has already been cloned, return it.
4. Otherwise:
   - Create a copy of the node.
   - Store it in the map.
   - Recursively clone all neighbors.
5. Return the cloned node.

Example:
Input graph:
1 -- 2
|    |
4 -- 3

Output:
A deep copy of the same graph structure.

Time Complexity:
- O(V + E)
  - V = number of nodes
  - E = number of edges

Space Complexity:
- O(V)
  - Hash map stores all cloned nodes
  - Recursion stack in the worst case
"""

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

if __name__ == "__main__":
    # Example usage would require graph construction
    pass
