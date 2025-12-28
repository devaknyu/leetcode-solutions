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

# Example usage
if __name__ == "__main__":
    # Helper function to build linked list
    def build_list(values):
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    # Helper function to print linked list
    def print_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

    # Example
    head = build_list([1, 2, 3, 4, 5])
    k = 2
    new_head = Solution().reverseKGroup(head, k)
    print_list(new_head)  # Expected: [2, 1, 4, 3, 5]