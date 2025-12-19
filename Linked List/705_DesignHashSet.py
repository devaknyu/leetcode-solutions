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
