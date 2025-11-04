from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node simplifies head removal
        tail = dummy

        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next
            head = head.next

        tail.next = None  # End the list cleanly
        return dummy.next
    
# Example usage
if __name__ == "__main__":
    def build_list(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def print_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        print(result)

    sol = Solution()
    head = build_list([1, 2, 6, 3, 4, 5, 6])
    new_head = sol.removeElements(head, 6)
    print_list(new_head)  # Expected output: [1, 2, 3, 4, 5]
