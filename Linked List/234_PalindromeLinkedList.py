from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Compare first and second halves
        first, last = head, prev
        while last:
            if first.val != last.val:
                return False
            first = first.next
            last = last.next

        return True
