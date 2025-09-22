from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper_fun(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper_fun(l, m - 1)
            root.right = helper_fun(m + 1, r)
            return root

        return helper_fun(0, len(nums) - 1)