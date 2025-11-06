from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# Example usage
if __name__ == "__main__":
    def build_list(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def print_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        print(result)

    sol = Solution()
    head = build_list([1, 2, 3, 4, 5])
    middle = sol.middleNode(head)
    print_list(middle)  # Expected output: [3, 4, 5]
    
    head2 = build_list([1, 2, 3, 4, 5, 6])
    middle2 = sol.middleNode(head2)
    print_list(middle2)  # Expected output: [4, 5, 6]
