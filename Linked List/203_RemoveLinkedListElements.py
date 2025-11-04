"""
LeetCode 203: Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Approach:
- We are given the head of a linked list and an integer `val`.  
  We must remove all nodes from the list that contain `val`.

Steps:
1. Create a `dummy` node to simplify edge cases (e.g., when the head node itself must be removed).
2. Use a `tail` pointer to build the new filtered list.
3. Traverse the original list (`head`):
   - If `head.val` is **not equal** to `val`, link it to the new list (`tail.next = head`) and move `tail` forward.
   - Otherwise, skip the node by moving `head` forward.
4. After traversal, set `tail.next = None` to ensure the new list terminates cleanly.
5. Return `dummy.next` — the head of the filtered list without unwanted elements.

Example:
Input:
  head = [1, 2, 6, 3, 4, 5, 6], val = 6
Process:
  → Skip nodes with value 6  
  → Keep nodes [1, 2, 3, 4, 5]
Output:
  [1, 2, 3, 4, 5]

Time Complexity: O(n) — one pass through the list  
Space Complexity: O(1) — in-place modification without extra storage
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node simplifies head removal
        tail = dummy

        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next
            head = head.next

        tail.next = None  # End the list cleanly
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
    head = build_list([1, 2, 6, 3, 4, 5, 6])
    new_head = sol.removeElements(head, 6)
    print_list(new_head)  # Expected output: [1, 2, 3, 4, 5]
