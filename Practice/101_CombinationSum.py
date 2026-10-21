from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Found a valid combination
            if total == target:
                res.append(cur.copy())
                return

            # Exceeded bounds or sum
            if i >= len(candidates) or total > target:
                return

            # Include current candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Exclude current candidate
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
