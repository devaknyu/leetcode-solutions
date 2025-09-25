from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row
        return res
    
    # Example run for local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.getRow(3))  # Expected [1, 3, 3, 1]