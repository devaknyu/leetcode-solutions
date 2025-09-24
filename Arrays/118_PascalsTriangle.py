
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]   # pad with zeros
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
    
    # Example run for local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))  # Expected [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]