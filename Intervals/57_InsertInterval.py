from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # Case 1: new interval is completely before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: current interval is completely before new interval
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # Case 3: overlapping intervals → merge
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        # If newInterval goes at the end
        res.append(newInterval)
        return res
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))  
    # Expected: [[1,5],[6,9]]

    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  
    # Expected: [[1,2],[3,10],[12,16]]
