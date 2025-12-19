"""
LeetCode 705: Design HashSet
https://leetcode.com/problems/design-hashset/

Approach:
- Design a HashSet without using built-in hash table libraries
- Use chaining with linked lists to handle collisions
- Array of linked lists (buckets) with fixed size
- Simple modulo hash function for distribution

Technique: Array of Linked Lists (Chaining)
1. Fixed size array (10⁴) of dummy head nodes for linked lists
2. Hash function: key % array_size
3. Each bucket contains linked list of elements with same hash
4. Operations traverse linked list for that bucket

Time Complexity (average): O(1) for add/remove/contains
Time Complexity (worst): O(n) if all keys hash to same bucket
Space Complexity: O(n) where n is number of unique keys
"""

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        # Create array of dummy head nodes
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        # Get bucket for this key
        curr = self.set[key % len(self.set)]
        # Traverse linked list to check if key exists
        while curr.next:
            if curr.next.key == key:
                return  # Key already exists
            curr = curr.next
        # Add new key at end of list
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        # Get bucket for this key
        curr = self.set[key % len(self.set)]
        # Traverse linked list to find key
        while curr.next:
            if curr.next.key == key:
                # Remove node by skipping it
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        # Get bucket for this key
        curr = self.set[key % len(self.set)]
        # Traverse linked list to find key
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False
    
# Example usage
if __name__ == "__main__":
    hashSet = MyHashSet()
    
    operations = [
        ("add", 1),
        ("add", 2),
        ("contains", 1, True),
        ("contains", 3, False),
        ("add", 2),
        ("contains", 2, True),
        ("remove", 2),
        ("contains", 2, False),
    ]
    
    for op in operations:
        if op[0] == "add":
            hashSet.add(op[1])
            print(f"add({op[1]})")
        elif op[0] == "remove":
            hashSet.remove(op[1])
            print(f"remove({op[1]})")
        elif op[0] == "contains":
            result = hashSet.contains(op[1])
            expected = op[2]
            status = "✓" if result == expected else "✗"
            print(f"contains({op[1]}) = {result} (Expected: {expected}) {status}")