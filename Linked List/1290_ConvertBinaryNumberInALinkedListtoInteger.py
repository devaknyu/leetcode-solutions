"""
LeetCode 1290: Convert Binary Number in a Linked List to Integer
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Approach:
- We are given a singly linked list where each node contains a binary digit (0 or 1).
- The binary number is represented from the most significant bit (head) to the least significant bit.
- We need to convert this binary representation to its decimal (integer) equivalent.

Technique: Bit Manipulation / Linear Traversal
1. Traverse the linked list from head to tail.
2. For each node, shift the current result left by 1 bit (multiply by 2) and add the current node's value.
3. This effectively builds the decimal value as we traverse through each bit.

Example:
Input: [1,0,1]
Process:
  Start: result = 0
  Node 1: result = 0*2 + 1 = 1
  Node 0: result = 1*2 + 0 = 2
  Node 1: result = 2*2 + 1 = 5
Output: 5

Input: [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Time Complexity: O(n) — traverse each node once
Space Complexity: O(1) — use only constant extra space
"""

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