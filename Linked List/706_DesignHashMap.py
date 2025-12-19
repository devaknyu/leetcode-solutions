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