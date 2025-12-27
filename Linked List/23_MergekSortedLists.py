from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list
        using divide and conquer.
        """

        # Edge case: empty input
        if not lists or len(lists) == 0:
            return None

        # Keep merging until one list remains
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))

            lists = merged_lists

        return lists[0]

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists using two pointers.
        """

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach remaining nodes
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
