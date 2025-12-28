"""
LeetCode 25: Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Problem Description:
- Given the head of a singly linked list, reverse the nodes of the list k at a time.
- Nodes that are left over (less than k) at the end should remain as-is.
- You may not alter node values; only pointers can be changed.

Approach:
- Reversing the entire list is not correct because we only reverse fixed-size groups.
- Instead, we:
  1. Process the list group by group
  2. For each group of size k:
     - Reverse the pointers within the group
     - Reconnect the group to the rest of the list
- A dummy node simplifies edge cases involving the head.

Key Observations:
- If fewer than k nodes remain, we stop processing.
- Reversal must be done in-place using pointer manipulation.
- Keeping track of group boundaries is critical to avoid breaking the list.

Technique: Linked List Traversal + In-place Reversal
1. Use a dummy node pointing to the head
2. Find the k-th node from the current group’s start
3. Reverse nodes between group start and group end
4. Reconnect the reversed group to the previous and next sections
5. Move to the next group

Time Complexity:
- O(n), where n is the number of nodes

Space Complexity:
- O(1), constant extra space
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses nodes of the linked list in groups of size k.
        """

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # ---------- Step 1: Find k-th node ----------
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # ---------- Step 2: Reverse the group ----------
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # ---------- Step 3: Reconnect ----------
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        """
        Returns the k-th node starting from curr.
        If fewer than k nodes remain, returns None.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# Example usage
if __name__ == "__main__":
    # Helper function to build linked list
    def build_list(values):
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    # Helper function to print linked list
    def print_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

    # Example
    head = build_list([1, 2, 3, 4, 5])
    k = 2
    new_head = Solution().reverseKGroup(head, k)
    print_list(new_head)  # Expected: [2, 1, 4, 3, 5]