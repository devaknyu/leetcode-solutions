"""
LeetCode 146: LRU Cache
https://leetcode.com/problems/lru-cache/

Problem Description:
- Design a data structure that follows the constraints of a
  Least Recently Used (LRU) cache.
- Implement the LRUCache class:
  * LRUCache(int capacity)
  * int get(int key)
  * void put(int key, int value)
- The cache should evict the least recently used item when capacity is exceeded.

Key Observations:
- We need O(1) time complexity for both get and put.
- A hash map provides O(1) lookup.
- A doubly linked list maintains usage order efficiently.

Approach:
- Use a hash map to store key → node mappings.
- Use a doubly linked list to track usage order:
  * Most recently used (MRU) near the right end
  * Least recently used (LRU) near the left end
- Use dummy head (left) and tail (right) nodes to simplify pointer handling.

Technique: Hash Map + Doubly Linked List
1. Hash map allows fast access to nodes
2. Doubly linked list maintains order of usage
3. On access or update, move node to MRU position
4. On overflow, evict LRU node

Time Complexity:
- get: O(1)
- put: O(1)

Space Complexity:
- O(capacity)
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # Dummy nodes
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from the linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node at the MRU position (right side)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        """
        Returns the value associated with the key if it exists,
        otherwise returns -1.
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the key-value pair.
        Evicts the least recently used item if capacity is exceeded.
        """
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Evict least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Example usage
if __name__ == "__main__":
    lru = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # Expected: 1

    lru.put(3, 3)      # Evicts key 2
    print(lru.get(2))  # Expected: -1

    lru.put(4, 4)      # Evicts key 1
    print(lru.get(1))  # Expected: -1
    print(lru.get(3))  # Expected: 3
    print(lru.get(4))  # Expected: 4