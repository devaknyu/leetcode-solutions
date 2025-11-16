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

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Helper functions
    def create_list(nums):
        dummy = ListNode()
        current = dummy
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return dummy.next
    
    def print_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
    # Test cases
    test_cases = [
        ([2,4,3], [5,6,4]),     # → [7,0,8] (342 + 465 = 807)
        ([0], [0]),              # → [0] (0 + 0 = 0)
        ([9,9,9], [1]),          # → [0,0,0,1] (999 + 1 = 1000)
    ]
    
    for l1_nums, l2_nums in test_cases:
        l1 = create_list(l1_nums)
        l2 = create_list(l2_nums)
        result = sol.addTwoNumbers(l1, l2)
        print(f"l1={l1_nums}, l2={l2_nums} → {print_list(result)}")