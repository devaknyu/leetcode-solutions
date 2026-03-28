"""
LeetCode 49: Group Anagrams
https://leetcode.com/problems/group-anagrams/

Approach:
- Group strings that are anagrams of each other
- Use character count tuples as keys in dictionary
- All anagrams will have identical character count tuples

Technique: Character Frequency Counting with Hash Map
1. For each string, create frequency count array of 26 letters
2. Convert count array to tuple (hashable) to use as dictionary key
3. Group strings with same character count tuple together

Time Complexity: O(n * k) where n is strings count, k is max string length
Space Complexity: O(n * k) for storing results
"""

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