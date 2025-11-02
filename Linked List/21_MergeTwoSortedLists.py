"""
LeetCode 21: Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Approach:
- We are given two sorted linked lists `list1` and `list2`.
- The goal is to merge them into one **sorted linked list** and return its head.

Steps:
1. Create a dummy node (`dummy`) that serves as a placeholder for the result list.
   - This helps avoid dealing with edge cases when initializing the head.
2. Maintain a pointer `tail` which always points to the **last node** of the merged list.
3. Traverse both lists simultaneously:
   - Compare the current node values of `list1` and `list2`.
   - Append the smaller node to `tail.next` and move that list’s pointer forward.
   - Move `tail` forward to the newly added node.
4. Once one list is exhausted, append the remaining part of the other list (since both are already sorted).
5. Return `dummy.next` (the real head of the merged list).

Example:
Input:
  list1 = [1, 2, 4]
  list2 = [1, 3, 4]
Process:
  → Compare 1 and 1 → take list2's 1
  → Compare 1 and 2 → take list1's 1
  → Compare 2 and 3 → take list1's 2
  → Compare 4 and 3 → take list2's 3
  → Compare 4 and 4 → take list1's 4
  → Attach remaining list2’s 4
Output:
  [1, 1, 2, 3, 4, 4]

Time Complexity: O(n + m) — traverse both lists once
Space Complexity: O(1) — in-place merging using pointers
"""


from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


# Example usage
if __name__ == "__main__":
    # Helper to build and print linked lists
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
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    print_list(merged)  # Expected output: [1, 1, 2, 3, 4, 4]