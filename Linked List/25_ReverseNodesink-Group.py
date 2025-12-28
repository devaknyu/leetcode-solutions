from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses nodes of the linked list in groups of size k.
        """

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # ---------- Step 1: Find k-th node ----------
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # ---------- Step 2: Reverse the group ----------
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # ---------- Step 3: Reconnect ----------
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        """
        Returns the k-th node starting from curr.
        If fewer than k nodes remain, returns None.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

