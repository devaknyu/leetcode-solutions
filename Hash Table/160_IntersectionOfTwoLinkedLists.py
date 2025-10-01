"""
LeetCode 160: Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Approach: Two-Pointer Switching
- Traverse both lists with two pointers.
- When one pointer reaches the end, redirect it to the other list's head.
- If lists intersect, pointers will eventually meet at intersection.
- If not, both will become None.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""


from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a  # Either the intersection node or None
    

# Example usage
if __name__ == "__main__":
    # Create intersection at node with value 8
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)

    # List A: 4 -> 1 -> 8 -> 4 -> 5
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common

    # List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common

    sol = Solution()
    result = sol.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected output: 8
