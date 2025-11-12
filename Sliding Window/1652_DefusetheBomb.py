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