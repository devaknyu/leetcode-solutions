class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            total = val_l1 + val_l2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
