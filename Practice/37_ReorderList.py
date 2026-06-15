from typing import Optional, ListNode
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the linked list in-place.
        Do not return anything, modify head directly.
        """

        # ---------- Step 1: Find the middle of the list ----------
        slow, fast = head, head.next

        # Move slow by 1 step and fast by 2 steps
        # When fast reaches the end, slow is at the midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ---------- Step 2: Reverse the second half ----------
        second = slow.next
        prev = slow.next = None  # Split the list into two halves

        while second:
            temp = second.next      # Store next node
            second.next = prev      # Reverse pointer
            prev = second           # Move prev forward
            second = temp           # Move second forward

        # ---------- Step 3: Merge the two halves ----------
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2

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
    Solution().reorderList(head)
    print_list(head)  # Expected: [1, 5, 2, 4, 3]