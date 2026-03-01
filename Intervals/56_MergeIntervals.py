from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # Overlapping intervals
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)

            # Non-overlapping interval
            else:
                output.append([start, end])

        return output
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    # Expected: [[1,6],[8,10],[15,18]]

    print(sol.merge([[1,4],[4,5]]))
    # Expected: [[1,5]]