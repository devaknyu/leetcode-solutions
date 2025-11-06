"""
LeetCode 876: Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Approach:
- We need to return the middle node of a singly linked list.
- If there are two middle nodes (i.e., the list has an even length), return the **second** one.

Technique: Two-Pointer (Tortoise and Hare)
1. Use two pointers:
   - `slow` → moves one step at a time.
   - `fast` → moves two steps at a time.
2. When `fast` reaches the end (or `fast.next` is None),
   `slow` will be at the middle of the list.
3. Return the `slow` pointer as the middle node.

Example:
Input:
  head = [1, 2, 3, 4, 5]
Process:
  slow → 1→2→3→4→5  
  fast → 1→3→5  
  When fast reaches the end, slow is at 3.
Output:
  [3, 4, 5]

Input (even length):
  head = [1, 2, 3, 4, 5, 6]
Output:
  [4, 5, 6]

Time Complexity: O(n) — traverse each node once  
Space Complexity: O(1) — use only two pointers
"""

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
