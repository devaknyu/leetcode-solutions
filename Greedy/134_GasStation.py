"""
LeetCode 134: Gas Station
https://leetcode.com/problems/gas-station/

Problem Description:
- There are `n` gas stations arranged in a circular route.
- `gas[i]` represents the amount of gas available at station `i`.
- `cost[i]` represents the gas required to travel from station `i` to station `i+1`.

Goal:
- Return the **starting gas station index** if you can travel around the circuit once.
- If it is impossible, return **-1**.

Examples:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
→ 3

Explanation:
Start at index 3:

Station 3 → gas = 4, cost = 1 → remaining = 3  
Station 4 → +5 -2 → remaining = 6  
Station 0 → +1 -3 → remaining = 4  
Station 1 → +2 -4 → remaining = 2  
Station 2 → +3 -5 → remaining = 0  

Successfully complete the circuit.

Example 2:
gas  = [2,3,4]
cost = [3,4,3]

Total gas = 9  
Total cost = 10  

Since total gas < total cost → impossible → return -1.

Approach (Greedy):

Key Observations:

1) If the **total gas is less than total cost**, completing the circuit
   is impossible regardless of starting point.

2) If we fail at station `i`, then **any station between the previous
   start and `i` cannot be a valid start**.

   Why?
   Because the total gas from that range was already insufficient.

Step-by-step logic:

1) Check feasibility:
      if sum(gas) < sum(cost):
          return -1

2) Maintain:
   total → current fuel balance
   res   → candidate starting station

3) Iterate through stations:

   At each station:
      total += gas[i] - cost[i]

4) If total becomes negative:
      we cannot start from `res`
      reset total = 0
      move start to next station
      res = i + 1

5) Continue until the end.

6) Return `res`.

Example:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Compute differences:
[-2, -2, -2, +3, +3]

Process:

i=0 → total = -2 → reset → start = 1  
i=1 → total = -2 → reset → start = 2  
i=2 → total = -2 → reset → start = 3  
i=3 → total = 3  
i=4 → total = 6  

Valid start = 3.

Time Complexity: O(n)
- Single pass through stations.

Space Complexity: O(1)
- Only constant variables are used.
"""

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = 0
        total = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Expected: 3
    print(sol.canCompleteCircuit([2,3,4], [3,4,3]))          # Expected: -1