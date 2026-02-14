from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        n, m = len(wordList), len(wordList[0])
        adj = [[] for _ in range(n)]
        mp = {wordList[i]: i for i in range(n)}

        # Build adjacency list (words differing by 1 char)
        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        diff += 1
                if diff == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        q = deque()
        visit = set()
        res = 1

        # Start BFS from words one step away from beginWord
        for i in range(m):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i + 1:]
                if word in mp:
                    q.append(mp[word])
                    visit.add(mp[word])

        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        return 0

# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),  # 5
        ("hit", "cog", ["hot","dot","dog","lot","log"]),        # 0
    ]

    for begin, end, words in test_cases:
        result = sol.ladderLength(begin, end, words)
        print(f"beginWord={begin}, endWord={end}")
        print(f"Output: {result}\n")