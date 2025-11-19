from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
    ]
    
    for strs in test_cases:
        print(f"Input: {strs}")
        result = sol.groupAnagrams(strs)
        print(f"Output: {result}\n")