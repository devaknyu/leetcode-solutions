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
