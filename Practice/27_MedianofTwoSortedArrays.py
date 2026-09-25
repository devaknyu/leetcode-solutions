from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Ensure A is smaller array for binary search efficiency
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        while True:
            i = (r + l) // 2  # Partition index for A
            j = half - i - 2  # Partition index for B
            
            # Handle edge cases with infinity bounds
            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i+1] if i+1 < len(A) else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j+1] if j+1 < len(B) else float("inf")
            
            # Check if partition is correct
            if A_left <= B_right and B_left <= A_right:
                # Odd total length
                if total % 2:
                    return min(A_right, B_right)
                # Even total length
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            # A_left too large, move left in A
            elif A_left > B_right:
                r = i - 1
            # A_right too small, move right in A
            else:
                l = i + 1