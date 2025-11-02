from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        tail = dummy

        while head:
            if tail.val != head.val:
                tail.next = head
                tail = tail.next
            head = head.next

        tail.next = None 
        return dummy.next
