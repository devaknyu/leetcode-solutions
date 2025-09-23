from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
    # Example run for local testing
if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))      # Output: ""
