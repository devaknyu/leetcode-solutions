class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
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