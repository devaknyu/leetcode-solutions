"""
LeetCode 1652: Defuse the Bomb
https://leetcode.com/problems/defuse-the-bomb/

Approach:
- We have a circular array `code` and need to replace each element with the sum of the next k elements.
- The array is circular, meaning elements wrap around from the end to the beginning.
- Three cases based on k:
  1. k > 0: Replace code[i] with sum of next k elements
  2. k < 0: Replace code[i] with sum of previous |k| elements  
  3. k = 0: Replace all elements with 0

Technique: Sliding Window on Circular Array
1. Use two pointers (l and r) to maintain a window of size |k|
2. Use modulo arithmetic to handle circular nature
3. For k > 0: Window represents the next k elements from current position
4. For k < 0: Window represents the previous |k| elements (equivalent to next |k| in reverse)
5. Update result array when window size equals |k|

Key Insight:
- For k < 0, finding previous |k| elements is same as finding next |k| elements 
  when traversing in reverse direction
- We can handle both cases with the same sliding window approach

Example:
Input: code = [5,7,1,4], k = 3
Process: Each element replaced with sum of next 3 elements
  code[0] = 7+1+4 = 12
  code[1] = 1+4+5 = 10  
  code[2] = 4+5+7 = 16
  code[3] = 5+7+1 = 13
Output: [12,10,16,13]

Input: code = [2,4,9,3], k = -2
Process: Each element replaced with sum of previous 2 elements
  code[0] = 3+9 = 12  (wrap around)
  code[1] = 2+3 = 5   (wrap around) 
  code[2] = 4+2 = 6
  code[3] = 9+4 = 13
Output: [12,5,6,13]

Time Complexity: O(n) - single pass through extended array
Space Complexity: O(n) - output array
"""

from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N
        
        # Special case: k = 0
        if k == 0:
            return res
        
        l = 0
        curr_sum = 0
        
        # Extend range to handle circular nature
        for r in range(N + abs(k)):
            curr_sum += code[r % N]
            
            # Maintain window size of abs(k)
            if r - l + 1 > abs(k):
                curr_sum -= code[l % N]
                l = (l + 1) % N
            
            # When window size equals abs(k), update result
            if r - l + 1 == abs(k):
                if k > 0:
                    # Store sum at position before window start
                    res[(l - 1) % N] = curr_sum
                elif k < 0:
                    # Store sum at position after window end  
                    res[(r + 1) % N] = curr_sum
        
        return res
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases with small examples
    test_cases = [
        ([5, 7, 1, 4], 3, [12, 10, 16, 13]),    # k > 0
        ([2, 4, 9, 3], -2, [12, 5, 6, 13]),     # k < 0  
        ([1, 2, 3, 4], 0, [0, 0, 0, 0]),        # k = 0
        ([1], 1, [0]),                           # single element
        ([1, 2], 1, [2, 1]),                     # two elements
    ]
    
    for code, k, expected in test_cases:
        result = sol.decrypt(code, k)
        status = "✓" if result == expected else "✗"
        print(f"code={code}, k={k} → {result} (Expected: {expected}) {status}")
    
    # Detailed explanation
    print("\n" + "="*50)
    print("Detailed example: code = [5, 7, 1, 4], k = 3")
    print("Circular array: [5, 7, 1, 4]")
    print("Each element replaced with sum of next 3 elements:")
    print("  code[0] = 7 + 1 + 4 = 12")
    print("  code[1] = 1 + 4 + 5 = 10") 
    print("  code[2] = 4 + 5 + 7 = 16")
    print("  code[3] = 5 + 7 + 1 = 13")
    print("Result: [12, 10, 16, 13]")