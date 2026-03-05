
"""
LeetCode 53: Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Problem Description:
- Given an integer array `nums`, find the contiguous subarray
  (containing at least one number) which has the largest sum.
- Return the maximum sum of that subarray.

Examples:
nums = [-2,1,-3,4,-1,2,1,-5,4]
→ 6
Explanation: [4,-1,2,1] has the largest sum = 6

nums = [1]
→ 1

nums = [5,4,-1,7,8]
→ 23

Approach (Kadane's Algorithm):

Key Idea:
- A negative running sum will only reduce the total of any
  future subarray. Therefore, if the current sum becomes negative,
  we reset it to 0 and start a new subarray.

Step-by-step logic:

1) Maintain two variables:
   curSum → sum of the current subarray
   maxSub → maximum subarray sum found so far

2) Iterate through each number `n` in the array.

3) If curSum becomes negative:
      reset it to 0
   because continuing with a negative sum would only
   decrease future sums.

4) Add current number:
      curSum += n

5) Update the global maximum:
      maxSub = max(maxSub, curSum)

Example:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Process:
curSum = 0

-2 → curSum = -2 → maxSub = -2
reset curSum to 0

1  → curSum = 1  → maxSub = 1
-3 → curSum = -2
reset curSum

4  → curSum = 4  → maxSub = 4
-1 → curSum = 3
2  → curSum = 5
1  → curSum = 6  → maxSub = 6
-5 → curSum = 1
4  → curSum = 5

Final answer = 6

Time Complexity: O(n)
- We iterate through the array once.

Space Complexity: O(1)
- Only constant extra variables are used.
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSub = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
    print(sol.maxSubArray([1]))                     # Expected: 1
    print(sol.maxSubArray([5,4,-1,7,8]))            # Expected: 23