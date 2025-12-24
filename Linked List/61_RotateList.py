from typing import Optional, ListNode
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotates the linked list to the right by k places
        and returns the new head.
        """

        # Edge case: empty list
        if not head:
            return head

        # ---------- Step 1: Find length and tail ----------
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # ---------- Step 2: Optimize k ----------
        k = k % length
        if k == 0:
            return head

        # ---------- Step 3: Find new tail ----------
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next

        # ---------- Step 4: Rotate ----------
        new_head = cur.next
        cur.next = None
        tail.next = head

        return new_head
