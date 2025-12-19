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
