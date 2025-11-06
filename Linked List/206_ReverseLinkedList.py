"""
LeetCode 206: Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Approach:
- We are given the head of a singly linked list, and we must reverse the list so that the head points to the last node.
- The task must be done **in-place** with **O(1) extra space**.

Steps:
1. Initialize two pointers:
   - `prev` → tracks the previous node (starts as `None`)
   - `current` → traverses the list starting from `head`
2. For each node:
   - Temporarily store the next node (`temp = current.next`)
   - Reverse the link (`current.next = prev`)
   - Move `prev` and `current` forward
3. When `current` becomes `None`, `prev` will point to the new head.
4. Return `prev` as the new head of the reversed list.

Example:
Input:
  head = [1, 2, 3, 4, 5]
Process:
  1 → 2 → 3 → 4 → 5  
  Reversing step-by-step gives → 5 → 4 → 3 → 2 → 1
Output:
  [5, 4, 3, 2, 1]

Time Complexity: O(n) — traverse each node once  
Space Complexity: O(1) — in-place reversal
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev
    
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
    reversed_head = sol.reverseList(head)
    print_list(reversed_head)  # Expected output: [5, 4, 3, 2, 1]