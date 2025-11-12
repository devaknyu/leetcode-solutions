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