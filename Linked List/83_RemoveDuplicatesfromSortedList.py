from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        tail = dummy

        while head:
            if tail.val != head.val:
                tail.next = head
                tail = tail.next
            head = head.next

        tail.next = None 
        return dummy.next
    
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
    head = build_list([1, 1, 2, 3, 3])
    deduped = sol.deleteDuplicates(head)
    print_list(deduped)  # Expected output: [1, 2, 3]