class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_t = {}
        seen_s = {}

        for i in range(len(s)):
            seen_t[t[i]] = seen_t.get(t[i],0) + 1
            seen_s[s[i]] = seen_s.get(s[i],0) + 1
        
        for c in seen_s:
            if seen_s[c] != seen_t.get(c,0):
                return False
        return True