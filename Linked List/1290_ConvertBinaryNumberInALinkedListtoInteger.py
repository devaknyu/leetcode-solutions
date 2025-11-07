from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        while head:
            result = result * 2 + head.val
            head = head.next
        return result

# Example usage
if __name__ == "__main__":
    def build_list(values):
        dummy = ListNode()
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    sol = Solution()
    
    # Test case 1: [1,0,1] → 5
    head1 = build_list([1, 0, 1])
    print(f"Binary [1,0,1] → Decimal: {sol.getDecimalValue(head1)}")  # Expected: 5
    
    # Test case 2: [0] → 0
    head2 = build_list([0])
    print(f"Binary [0] → Decimal: {sol.getDecimalValue(head2)}")  # Expected: 0
    
    # Test case 3: [1] → 1
    head3 = build_list([1])
    print(f"Binary [1] → Decimal: {sol.getDecimalValue(head3)}")  # Expected: 1
    
    # Test case 4: [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0] → 18880
    head4 = build_list([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
    print(f"Binary [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0] → Decimal: {sol.getDecimalValue(head4)}")  # Expected: 18880