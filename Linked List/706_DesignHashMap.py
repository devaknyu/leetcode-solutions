"""
LeetCode 706: Design HashMap
https://leetcode.com/problems/design-hashmap/

Approach:
- Design a HashMap without using built-in hash table libraries
- Key-value storage using chaining with linked lists
- Array of linked lists (buckets) with fixed size
- Simple modulo hash function for distribution

Technique: Array of Linked Lists (Chaining)
1. Fixed size array (10⁴) of dummy head nodes for linked lists
2. Hash function: key % array_size
3. Each bucket contains linked list of key-value pairs with same hash
4. Operations traverse linked list for that bucket

Time Complexity (average): O(1) for put/get/remove
Time Complexity (worst): O(n) if all keys hash to same bucket
Space Complexity: O(n) where n is number of unique keys
"""
class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        # Create array of dummy head nodes
        self.map = [ListNode() for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        # Get bucket for this key
        curr = self.map[key % len(self.map)]
        # Traverse linked list
        while curr.next:
            if curr.next.key == key:
                # Key exists, update value
                curr.next.val = value
                return
            curr = curr.next
        # Key doesn't exist, add new node
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # Get bucket for this key
        curr = self.map[key % len(self.map)]
        # Traverse linked list
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        # Key not found
        return -1

    def remove(self, key: int) -> None:
        # Get bucket for this key
        curr = self.map[key % len(self.map)]
        # Traverse linked list
        while curr and curr.next:
            if curr.next.key == key:
                # Remove node by skipping it
                curr.next = curr.next.next
                return
            curr = curr.next

# Example usage
if __name__ == "__main__":
    hashMap = MyHashMap()
    
    operations = [
        ("put", 1, 1),
        ("put", 2, 2),
        ("get", 1, 1),
        ("get", 3, -1),
        ("put", 2, 1),
        ("get", 2, 1),
        ("remove", 2),
        ("get", 2, -1),
    ]
    
    for op in operations:
        if op[0] == "put":
            hashMap.put(op[1], op[2])
            print(f"put({op[1]}, {op[2]})")
        elif op[0] == "get":
            result = hashMap.get(op[1])
            expected = op[2]
            status = "✓" if result == expected else "✗"
            print(f"get({op[1]}) = {result} (Expected: {expected}) {status}")
        elif op[0] == "remove":
            hashMap.remove(op[1])
            print(f"remove({op[1]})")