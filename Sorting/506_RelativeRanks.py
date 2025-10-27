"""
LeetCode 506: Relative Ranks
https://leetcode.com/problems/relative-ranks/

Approach:
- We are given a list of athletes' scores, and we need to assign ranks based on their performance.
- The highest score gets "Gold Medal", the second "Silver Medal", and the third "Bronze Medal".
- All other athletes get their numerical rank (4th, 5th, etc.).

Steps:
1. Sort the `score` list in **descending order** to determine rank order.
2. Create a dictionary `rank_map` that maps each score to its corresponding rank string.
   - Use special labels for the top 3 ranks.
   - For others, assign rank as a string of their position + 1.
3. Iterate through the original `score` list and build the `result` by mapping each score to its rank.
4. Return the `result`.

Example:
Input:
  score = [5, 4, 3, 2, 1]
Output:
  ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation:
  The highest score (5) gets Gold, next (4) gets Silver, etc.

Time Complexity: O(n log n) — for sorting
Space Complexity: O(n) — for the rank mapping
"""

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {}

        for i, val in enumerate(sorted_score):
            if i == 0:
                rank_map[val] = "Gold Medal"
            elif i == 1:
                rank_map[val] = "Silver Medal"
            elif i == 2:
                rank_map[val] = "Bronze Medal"
            else:
                rank_map[val] = str(i + 1)
        
        result = [rank_map[i] for i in score]
        return result
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findRelativeRanks([5, 4, 3, 2, 1]))   # Expected: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    print(sol.findRelativeRanks([10, 3, 8, 9, 4]))  # Expected: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    print(sol.findRelativeRanks([1]))               # Expected: ["Gold Medal"]