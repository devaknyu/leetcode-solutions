from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            # Found a valid combination
            if total == target:
                res.append(cur.copy())
                return

            # Exceeded bounds or sum
            if i >= len(candidates) or total > target:
                return

            # Include current candidate (can only be used once)
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # Backtrack
            cur.pop()

            # Skip all duplicate values
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Exclude current candidate and move forward
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res