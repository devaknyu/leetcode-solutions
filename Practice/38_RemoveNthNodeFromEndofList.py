from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of the list
        and returns the head of the modified list.
        """

        # Dummy node handles edge cases (e.g., removing head)
        dummy = ListNode(0, head)

        # Left and right pointers
        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the target node
        left.next = left.next.next

        # Return the new head
        return dummy.next

# Example usage
if __name__ == "__main__":
    # Helper function to build a linked list
    def build_list(values):
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    # Helper function to print a linked list
    def print_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

    # Example
    head = build_list([1, 2, 3, 4, 5])
    n = 2
    head = Solution().removeNthFromEnd(head, n)
    print_list(head)  # Expected: [1, 2, 3, 5]