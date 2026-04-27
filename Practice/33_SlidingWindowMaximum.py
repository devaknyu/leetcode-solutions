import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # stores indices
        l = r = 0
        
        while r < len(nums):
            # Remove smaller elements from back of deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # Remove elements outside current window from front
            if q[0] < l:
                q.popleft()
            
            # When window reaches size k, add maximum to output
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
            
        return output

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),  # → [3, 3, 5, 5, 6, 7]
        ([1], 1),                         # → [1]
        ([1, -1], 1),                     # → [1, -1]
        ([7, 2, 4], 2),                   # → [7, 4]
    ]
    
    for nums, k in test_cases:
        print(f"nums={nums}, k={k}")
        result = sol.maxSlidingWindow(nums, k)
        print(f"Maximums: {result}\n")