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