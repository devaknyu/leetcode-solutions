"""
LeetCode 83: Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Approach:
- We are given a **sorted** linked list and need to remove all duplicate elements such that each element appears only once.
- Since the list is sorted, all duplicates will appear **next to each other**, so we can remove them in a single pass.

Steps:
1. Create a `dummy` node to simplify pointer management.
2. Use a pointer `tail` to track the **last unique node** in the result list.
3. Traverse the original list (`head`):
   - If `tail.val` is different from `head.val`, link the node (`tail.next = head`) and move `tail` forward.
   - If they are equal, skip the node by advancing `head`.
4. After traversal, set `tail.next = None` to terminate the list properly.
5. Return `dummy.next` as the head of the deduplicated linked list.

Example:
Input:
  head = [1, 1, 2, 3, 3]
Process:
  → Compare 1 and 1 → skip duplicate
  → Compare 1 and 2 → keep 2
  → Compare 2 and 3 → keep 3
  → Compare 3 and 3 → skip duplicate
Output:
  [1, 2, 3]

Time Complexity: O(n) — traverse the list once
Space Complexity: O(1) — modify in place without extra data structures
"""

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