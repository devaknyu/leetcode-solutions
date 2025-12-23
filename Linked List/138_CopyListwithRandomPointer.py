from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Returns a deep copy of the linked list.
        """

        # Map original nodes to their copies
        old_to_copy = {None: None}

        # ---------- First pass: copy all nodes ----------
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next

        # ---------- Second pass: assign next and random pointers ----------
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        # Return copied head
        return old_to_copy[head]

# Example usage
if __name__ == "__main__":
    # Helper function to print list with random pointers
    def print_list(head):
        curr = head
        while curr:
            random_val = curr.random.val if curr.random else None
            print(f"Node({curr.val}) -> Random({random_val})")
            curr = curr.next
        print()

    # Build example list
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    copied_head = Solution().copyRandomList(node1)

    print("Original list:")
    print_list(node1)

    print("Copied list:")
    print_list(copied_head)