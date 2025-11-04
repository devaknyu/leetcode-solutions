"""
LeetCode 234: Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Approach:
- We need to determine if a singly linked list reads the same forward and backward.
- The challenge is to do this efficiently **in O(n) time and O(1) space**.

Steps:
1. **Find the middle of the linked list** using the fast and slow pointer approach:
   - Move `fast` by two steps and `slow` by one step each iteration.
   - When `fast` reaches the end, `slow` will be at the midpoint.
2. **Reverse the second half** of the linked list starting from the `slow` pointer.
3. **Compare the first half and the reversed second half** node by node:
   - If all corresponding values match, the list is a palindrome.
   - If any mismatch is found, return `False`.
4. Optionally, the list can be restored to its original form by reversing the second half again (not required by LeetCode).
5. Return `True` if all checks pass.

Example:
Input:
  head = [1, 2, 2, 1]
Process:
  - Find middle → slow at second 2
  - Reverse second half → [1, 2]
  - Compare halves → [1, 2] == [1, 2]
Output:
  True

Time Complexity: O(n) — one pass to find the middle + one to reverse + one to compare  
Space Complexity: O(1) — in-place reversal and comparison
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Compare first and second halves
        first, last = head, prev
        while last:
            if first.val != last.val:
                return False
            first = first.next
            last = last.next

        return True
    
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
    head1 = build_list([1, 2, 2, 1])
    head2 = build_list([1, 2])
    print(sol.isPalindrome(head1))  # Expected output: True
    print(sol.isPalindrome(head2))  # Expected output: False