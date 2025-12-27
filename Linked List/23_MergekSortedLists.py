"""
LeetCode 23: Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Problem Description:
- You are given an array of k linked lists.
- Each linked list is sorted in ascending order.
- Merge all the linked lists into one sorted linked list and return it.

Approach:
- Merging lists one by one is inefficient.
- Instead, we use a divide-and-conquer approach similar to merge sort.
- At each step, we merge pairs of linked lists until only one list remains.

Key Observations:
- Each linked list is already sorted.
- Merging two sorted linked lists can be done in linear time.
- Pairwise merging reduces the total number of merge operations.
- The number of lists reduces by half after each iteration.

Technique: Divide and Conquer + Two Pointer Linked List Merge
1. While there is more than one list:
   - Merge lists in pairs (list[0] with list[1], list[2] with list[3], etc.)
2. Use a helper function to merge two sorted linked lists.
3. Repeat until one merged list remains.

Time Complexity:
- O(N log k)
  where N is the total number of nodes
  and k is the number of linked lists

Space Complexity:
- O(1) extra space (excluding output list)
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list
        using divide and conquer.
        """

        # Edge case: empty input
        if not lists or len(lists) == 0:
            return None

        # Keep merging until one list remains
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))

            lists = merged_lists

        return lists[0]

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists using two pointers.
        """

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach remaining nodes
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

# Example usage
if __name__ == "__main__":
    # Helper function to build a linked list
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
    lists = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6])
    ]

    merged = Solution().mergeKLists(lists)
    print_list(merged)  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]

