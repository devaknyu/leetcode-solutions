from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Detection
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

        # Alternative Hash Set Approach:
        # visited = set()
        # current = head
        # while current:
        #     if current in visited:
        #         return True
        #     visited.add(current)
        #     current = current.next
        # return False
