from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))  # Expected: [9,7,8]
    print(sol.partitionLabels("eccbbbbdec"))                 # Expected: [10]