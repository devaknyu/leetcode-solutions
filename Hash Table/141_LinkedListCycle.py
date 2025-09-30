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

# Example tests (manually constructed)
if __name__ == "__main__":
    # Create a linked list with a cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
    head = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node_4 = ListNode(-4)
    head.next = node2
    node2.next = node0
    node0.next = node_4
    node_4.next = node2  # creates cycle

    sol = Solution()
    print(sol.hasCycle(head))  # Expected True

    # Create a linked list with no cycle: 1 -> 2 -> None
    head2 = ListNode(1)
    node2b = ListNode(2)
    head2.next = node2b
    print(sol.hasCycle(head2))  # Expected False