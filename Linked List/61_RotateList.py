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
    head = Solution().rotateRight(head, k)
    print_list(head)  # Expected: [4, 5, 1, 2, 3]
